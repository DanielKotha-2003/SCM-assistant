# 🏢 Oracle SCM Learning Platform

An interactive web application built with **Streamlit** and powered by **Google Gemini AI** to help students and freshers understand Oracle EBS and Oracle Fusion Cloud business transaction flows.

# **Live application:** https://scm-assistant.streamlit.app/ [Hosted on streamlit community cloud] 

## 📋 Features

### Core Functionality
- **Multi-Flow Support**: Procure-to-Pay (P2P), Order-to-Cash (O2C), Plan-to-Produce
- **AI-Powered Explanations**: Leverages Google Gemini API for intelligent responses
- **Tab-Based UI**: Organized information across four tabs:
  - 📖 **Definition**: Simple, one-sentence explanation
  - 🏭 **Business Context**: Real-world scenario and business logic
  - 🗄️ **Technical Details**: Oracle tables and SQL examples
  - 🔄 **Flow Navigation**: Previous and next steps in the flow

### User Experience
- 🔐 Secure API key input (password field)
- 📊 Business flow selector dropdown
- 💬 Natural language query input
- 📚 Quick reference guide for complete flows
- 🎨 Professional Oracle-themed UI

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd "oracle-scm-assistant"
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the application:**
   - Open your browser and go to `http://localhost:8501`
   - Enter your Gemini API key in the sidebar
   - Select a business flow
   - Ask your question!

## 📝 Usage Examples

### For Specific Steps
- "Explain Purchase Order Creation in P2P"
- "What is 3-way match in procurement?"
- "Describe the invoice matching process"

### For Vague Queries
- "What is P2P?" → Returns complete P2P flow
- "Explain O2C" → Returns complete O2C flow
- "What is Plan-to-Produce?" → Returns complete flow

## 🏗️ Project Structure

```
SCM/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

## 📚 Business Flows Covered

### Procure-to-Pay (P2P)
1. Purchase Requisition Creation
2. Purchase Order Generation
3. Goods Receipt/PO Receipt
4. Three-Way Match
5. Invoice Matching & Receipt
6. Payment Processing
7. Payment Reconciliation

### Order-to-Cash (O2C)
1. Sales Quote Creation
2. Sales Order Entry
3. Order Reservation & Allocation
4. Picking & Staging
5. Packing & Labeling
6. Shipment
7. Invoice Generation
8. Accounts Receivable Recording
9. Collection & Payment

### Plan-to-Produce
1. Demand Forecasting
2. Production Planning
3. Master Scheduling
4. Material Requirements Planning (MRP)
5. Manufacturing Order Release
6. Component Picking
7. Manufacturing Execution
8. Quality Inspection
9. Completion & Receipt
10. Inventory Costing

## 🔒 Security

- **API Key Protection**: Streamlit's password input field securely masks the API key
- **No Key Storage**: API keys are never logged or persisted
- **Runtime Configuration**: API key is only used during the current session

## 🛠️ Technical Details

### Oracle Tables Referenced
The platform covers explanations involving:
- **Procurement**: PO_HEADERS_ALL, PO_LINES_ALL, RCV_TRANSACTIONS
- **Sales**: OE_ORDER_HEADERS_ALL, OE_ORDER_LINES_ALL, WSH_DELIVERIES
- **Manufacturing**: WIP_ENTITIES, WIP_JOB_SCHEDULE_INTERFACE
- **Financials**: AP_INVOICES_ALL, AR_TRANSACTION_HISTORY_ALL


## 🎯 Tone & Approach

- **Professional & Encouraging**: Mentor-style guidance
- **Beginner-Friendly**: Simple analogies with technical accuracy
- **Business-First**: Business meaning before technical implementation
- **Clear Distinctions**: Separates Business User actions from System/Workflow actions

## 🤖 AI Engine

- **Model**: Google Gemini 2.5 Flash
- **Capabilities**: 
  - Natural language understanding of Oracle SCM concepts
  - Contextual explanations based on selected flow
  - Technical accuracy with business relevance

## 📖 Documentation

For more information about:
- **Streamlit**: https://docs.streamlit.io/
- **Google Gemini API**: https://ai.google.dev/docs/
- **Oracle SCM**: [Oracle Help Center](https://docs.oracle.com/search/?q=SCM)

## 💡 Tips for Best Results

1. **Be Specific**: Ask about specific steps rather than broad topics
2. **Use Flow Context**: Select the relevant flow before asking
3. **Follow Suggestions**: Use quick reference to explore related steps
4. **Ask for SQL**: Request SQL examples for technical understanding

## 🐛 Troubleshooting

### "Gemini API Key is required"
- Ensure you've entered a valid API key in the sidebar
- Check that the key is correctly formatted

### "Failed to parse response"
- The API may have rate limits—wait a moment and try again
- Try a more specific question if the query is too vague

### Application won't start
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Ensure Python version is 3.9+

## 📞 Support

For issues or questions:
- Check the troubleshooting section above
- Review your Gemini API key validity
- Consult Oracle documentation for specific SCM details

## 📄 License

Educational resource for learning Oracle SCM flows.

## 🙏 Acknowledgments

Built with:
- [Streamlit](https://streamlit.io/) - Web application framework
- [Google Gemini AI](https://ai.google.dev/) - Large language model
- Oracle Documentation - [Business process knowledge](https://docs.oracle.com/search/?q=SCM)

---

**Version**: 1.0  
**Last Updated**: January 2026  
**Status**: Active Development




