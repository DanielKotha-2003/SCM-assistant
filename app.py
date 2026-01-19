import streamlit as st
import google.generativeai as genai
from typing import Generator

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Oracle SCM Knowledge Engine",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏢 Oracle SCM Learning Platform")
st.markdown("*Expert guidance on Oracle EBS and Fusion Cloud business flows*")

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Gemini API Key Input
    api_key = st.text_input(
        "🔑 Gemini API Key",
        type="password",
        help="Enter your Google Gemini API key to enable explanations"
    )
    
    # Business Flow Selector
    selected_flow = st.selectbox(
        "📊 Select Business Flow",
        options=[
            "Procure-to-Pay (P2P)",
            "Order-to-Cash (O2C)",
            "Plan-to-Produce"
        ],
        help="Choose the business flow context for explanations"
    )
    
    st.divider()
    st.markdown("### About")
    st.markdown(
        """
        This platform helps you understand Oracle SCM flows through:
        - **Simple Definition**: Plain English explanation
        - **Business Context**: Real-world scenarios
        - **Technical Details**: Oracle tables and SQL
        - **Flow Navigation**: Previous and next steps
        """
    )

# ============================================================================
# VALIDATION & API INITIALIZATION
# ============================================================================
if not api_key:
    st.error("⚠️ Gemini API Key is required. Please enter your API key in the sidebar to proceed.")
    st.stop()

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error(f"❌ Failed to initialize Gemini API: {str(e)}")
    st.stop()

# ============================================================================
# SYSTEM PROMPT & KNOWLEDGE BASE
# ============================================================================
SYSTEM_PROMPT = f"""You are an Expert Oracle SCM Consultant and Mentor specializing in Oracle EBS and Oracle Fusion Cloud.
Your role is to help students and freshers understand Oracle SCM business transaction flows clearly.

CURRENT FLOW CONTEXT: {selected_flow}

CRITICAL REQUIREMENTS:
Format your response with these exact sections. Use the delimiter lines as shown:

[DEFINITION]
One concise sentence explaining the step in plain English for non-technical learners.

[BUSINESS_CONTEXT]
Short real-world business scenario explaining why this step exists and who performs it. Clearly distinguish between Business User actions and Background System/Oracle workflow actions.

[ORACLE_TABLES]
List of primary Oracle EBS/Fusion database tables involved (comma-separated or one per line).

[PREVIOUS_STEP]
The immediate upstream step in the business flow.

[NEXT_STEP]
The immediate downstream step in the business flow.

TONE & STYLE:
- Professional, encouraging, mentor-style
- Use simple analogies with immediate explanations for technical terms
- Beginner-friendly yet technically accurate
- Focus on business meaning first, technical implementation second

GUIDELINES:
- If user asks a high-level or vague question, respond with the complete {selected_flow} flow as a numbered list
- For SQL requests, provide simple examples: SELECT * FROM <TABLE_NAME>;
- NEVER mention, repeat, or expose any API keys
- Always follow the defined response structure exactly

FLOW-SPECIFIC KNOWLEDGE:
- P2P (Procure-to-Pay): Requisition Creation, PO creation, receipt, 3-way match, invoice, payment
- O2C (Order-to-Cash): Quote, Order, Picking, Packing, Shipping, Invoice, AR, Collection
- Plan-to-Produce: Forecast, Planning, MRP, Manufacturing, Costing, Completion"""

# ============================================================================
# FLOW DEFINITIONS FOR VAGUE QUESTIONS
# ============================================================================
FLOW_STEPS = {
    "Procure-to-Pay (P2P)": [
        "Purchase Requisition Creation",
        "Purchase Order Generation",
        "Goods Receipt/PO Receipt",
        "Three-Way Match",
        "Invoice Matching & Receipt",
        "Payment Processing",
        "Payment Reconciliation"
    ],
    "Order-to-Cash (O2C)": [
        "Sales Quote Creation",
        "Sales Order Entry",
        "Order Reservation & Allocation",
        "Picking & Staging",
        "Packing & Labeling",
        "Shipment",
        "Invoice Generation",
        "Accounts Receivable Recording",
        "Collection & Payment"
    ],
    "Plan-to-Produce": [
        "Demand Forecasting",
        "Production Planning",
        "Master Scheduling",
        "Material Requirements Planning (MRP)",
        "Manufacturing Order Release",
        "Component Picking",
        "Manufacturing Execution",
        "Quality Inspection",
        "Completion & Receipt",
        "Inventory Costing"
    ]
}

# ============================================================================
# MAIN APPLICATION INTERFACE
# ============================================================================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Chat with Oracle SCM Expert")
    st.markdown("*Ask questions about Oracle EBS and Fusion Cloud processes*")

with col2:
    st.write("")

# ============================================================================
# CHAT FUNCTIONS
# ============================================================================
def format_messages(messages):
    """Format chat history for Gemini API"""
    formatted = [{"role": "user", "parts": [{"text": SYSTEM_PROMPT}]}]
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        formatted.append({"role": role, "parts": [{"text": msg["content"]}]})
    return formatted

def gemini_generator(messages: list) -> Generator:
    """Generate streaming responses from Gemini"""
    chat = model.start_chat(history=format_messages(messages))
    
    user_input = messages[-1]["content"]  
    response = chat.send_message(user_input, stream=True)

    for chunk in response:
        yield chunk.text

# ============================================================================
# INITIALIZE SESSION STATE
# ============================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================================
# DISPLAY CHAT HISTORY
# ============================================================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============================================================================
# CHAT INPUT & RESPONSE
# ============================================================================
if prompt := st.chat_input("Ask me about Oracle SCM processes..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Gemini
    with st.chat_message("assistant"):
        response = st.write_stream(gemini_generator(st.session_state.messages))
    
    # Save response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# ============================================================================
# QUICK REFERENCE SECTION
# ============================================================================
st.divider()
with st.expander("📚 Quick Reference - Full Flow for " + selected_flow):
    st.markdown(f"### {selected_flow} Flow Steps:")
    for i, step in enumerate(FLOW_STEPS.get(selected_flow, []), 1):
        st.markdown(f"{i}. **{step}**")

# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    <p>Oracle SCM Learning Platform v1.0 | Powered by Google Gemini</p>
    <p>Educational resource for understanding Oracle EBS and Fusion Cloud</p>
    </div>
    """,
    unsafe_allow_html=True
)
