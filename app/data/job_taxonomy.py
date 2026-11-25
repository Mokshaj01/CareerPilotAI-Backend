"""
CareerPilotAI - Central Job Fields Taxonomy

Master list of professional fields and their job subfields.
Canonical roles and alternative titles will be added in later stages.

"""

TAXONOMY_VERSION = "1.0.0"

PROFESSIONAL_FIELDS = [
    {"id": "technology_it", "name": "Technology & IT"},
    {"id": "data_analytics", "name": "Data & Analytics"},
    {"id": "engineering_manufacturing", "name": "Engineering & Manufacturing"},
    {"id": "finance_accounting", "name": "Finance & Accounting"},
    {"id": "sales_business_development", "name": "Sales & Business Development"},
    {"id": "marketing_communications", "name": "Marketing & Communications"},
    {"id": "human_resources", "name": "Human Resources"},
    {"id": "operations_administration", "name": "Operations & Administration"},
    {"id": "customer_support_bpo", "name": "Customer Support & BPO"},
    {"id": "product_project_management", "name": "Product & Project Management"},
    {"id": "healthcare_life_sciences", "name": "Healthcare & Life Sciences"},
    {"id": "other_professional_roles", "name": "Other Professional Roles"},
    {"id": "education_training", "name": "Education & Training"},
    {"id": "legal_compliance", "name": "Legal & Compliance"},
    {"id": "design_arts_creative", "name": "Design, Arts & Creative"},
    {"id": "hospitality_retail_skilled_trades", "name": "Hospitality, Retail & Skilled Trades"},
]

SUBFIELDS_BY_FIELD = {
    "technology_it": [
        {"id": "artificial_intelligence_generative_ai", "name": "Artificial Intelligence & Generative AI"},
        {"id": "machine_learning_deep_learning", "name": "Machine Learning & Deep Learning"},
        {"id": "data_science_applied_ai", "name": "Data Science & Applied AI"},
        {"id": "software_development", "name": "Software Development"},
        {"id": "frontend_development", "name": "Frontend Development"},
        {"id": "backend_development", "name": "Backend Development"},
        {"id": "full_stack_development", "name": "Full Stack Development"},
        {"id": "mobile_application_development", "name": "Mobile Application Development"},
        {"id": "web_development", "name": "Web Development"},
        {"id": "cloud_computing_architecture", "name": "Cloud Computing & Architecture"},
        {"id": "devops_site_reliability_engineering", "name": "DevOps & Site Reliability Engineering"},
        {"id": "cybersecurity_information_security", "name": "Cybersecurity & Information Security"},
        {"id": "networking_infrastructure", "name": "Networking & Infrastructure"},
        {"id": "database_data_administration", "name": "Database & Data Administration"},
        {"id": "software_testing_quality_assurance", "name": "Software Testing & Quality Assurance"},
        {"id": "embedded_systems_firmware", "name": "Embedded Systems & Firmware"},
        {"id": "hardware_semiconductor_engineering", "name": "Hardware & Semiconductor Engineering"},
        {"id": "enterprise_applications_erp", "name": "Enterprise Applications & ERP"},
        {"id": "it_support_technical_services", "name": "IT Support & Technical Services"},
        {"id": "it_management_architecture", "name": "IT Management & Architecture"},
    ],
    
      "data_analytics": [
        {"id": "data_analysis_reporting", "name": "Data Analysis & Reporting"},
        {"id": "business_intelligence_visualization", "name": "Business Intelligence & Visualization"},
        {"id": "data_engineering", "name": "Data Engineering"},
        {"id": "big_data_distributed_systems", "name": "Big Data & Distributed Systems"},
        {"id": "data_warehousing_architecture", "name": "Data Warehousing & Architecture"},
        {"id": "business_product_analytics", "name": "Business & Product Analytics"},
        {"id": "statistical_quantitative_analytics", "name": "Statistical & Quantitative Analytics"},
        {"id": "marketing_financial_operations_analytics", "name": "Marketing, Financial & Operations Analytics"},
        {"id": "data_governance_quality", "name": "Data Governance & Quality"},
        {"id": "analytics_engineering_data_management", "name": "Analytics Engineering & Data Management"},
    ],
      
       "engineering_manufacturing": [
        {"id": "mechanical_engineering", "name": "Mechanical Engineering"},
        {"id": "electrical_electronics_engineering", "name": "Electrical & Electronics Engineering"},
        {"id": "civil_structural_engineering", "name": "Civil & Structural Engineering"},
        {"id": "chemical_process_engineering", "name": "Chemical & Process Engineering"},
        {"id": "industrial_production_engineering", "name": "Industrial & Production Engineering"},
        {"id": "manufacturing_automation", "name": "Manufacturing & Automation"},
        {"id": "automotive_transportation_engineering", "name": "Automotive & Transportation Engineering"},
        {"id": "materials_metallurgical_engineering", "name": "Materials & Metallurgical Engineering"},
        {"id": "quality_testing_reliability_engineering", "name": "Quality, Testing & Reliability Engineering"},
        {"id": "engineering_design_project_execution", "name": "Engineering Design & Project Execution"},
    ],
       
       "finance_accounting": [
        {"id": "accounting_bookkeeping", "name": "Accounting & Bookkeeping"},
        {"id": "audit_assurance", "name": "Audit & Assurance"},
        {"id": "taxation", "name": "Taxation"},
        {"id": "financial_management_controlling", "name": "Financial Management & Controlling"},
        {"id": "financial_planning_analysis", "name": "Financial Planning & Analysis"},
        {"id": "banking_credit", "name": "Banking & Credit"},
        {"id": "investment_asset_management", "name": "Investment & Asset Management"},
        {"id": "insurance_risk_management", "name": "Insurance & Risk Management"},
    ],
       
       "sales_business_development": [
        {"id": "business_development_partnerships", "name": "Business Development & Partnerships"},
        {"id": "inside_field_sales", "name": "Inside & Field Sales"},
        {"id": "enterprise_b2b_sales", "name": "Enterprise & B2B Sales"},
        {"id": "account_management_client_relations", "name": "Account Management & Client Relations"},
        {"id": "sales_operations_enablement", "name": "Sales Operations & Enablement"},
        {"id": "channel_retail_sales", "name": "Channel & Retail Sales"},
        {"id": "presales_solutions_consulting", "name": "Pre-Sales & Solutions Consulting"},
    ],
           
       "marketing_communications": [
        {"id": "digital_performance_marketing", "name": "Digital & Performance Marketing"},
        {"id": "brand_product_marketing", "name": "Brand & Product Marketing"},
        {"id": "content_copywriting_communications", "name": "Content, Copywriting & Communications"},
        {"id": "public_relations_corporate_communications", "name": "Public Relations & Corporate Communications"},
        {"id": "market_research_consumer_insights", "name": "Market Research & Consumer Insights"},
        {"id": "marketing_strategy_operations", "name": "Marketing Strategy & Operations"},
    ],  
       
       "human_resources": [
        {"id": "talent_acquisition_recruitment", "name": "Talent Acquisition & Recruitment"},
        {"id": "hr_operations_administration", "name": "HR Operations & Administration"},
        {"id": "learning_development", "name": "Learning & Development"},
        {"id": "compensation_benefits_payroll", "name": "Compensation, Benefits & Payroll"},
        {"id": "employee_relations_engagement", "name": "Employee Relations & Engagement"},
        {"id": "hr_strategy_business_partnering", "name": "HR Strategy & Business Partnering"},
    ],  
       
      "operations_administration": [
        {"id": "business_operations_process_management", "name": "Business Operations & Process Management"},
        {"id": "office_administration_executive_support", "name": "Office Administration & Executive Support"},
        {"id": "supply_chain_logistics_distribution", "name": "Supply Chain, Logistics & Distribution"},
        {"id": "procurement_purchasing", "name": "Procurement & Purchasing"},
        {"id": "facilities_workplace_management", "name": "Facilities & Workplace Management"},
        {"id": "process_improvement_business_excellence", "name": "Process Improvement & Business Excellence"},
    ], 
           
      "customer_support_bpo": [
        {"id": "customer_service_customer_care", "name": "Customer Service & Customer Care"},
        {"id": "contact_center_call_center_operations", "name": "Contact Center & Call Center Operations"},
        {"id": "technical_product_support", "name": "Technical & Product Support"},
        {"id": "customer_success_client_services", "name": "Customer Success & Client Services"},
        {"id": "back_office_transaction_processing", "name": "Back-Office & Transaction Processing"},
        {"id": "customer_experience_quality_escalations", "name": "Customer Experience, Quality & Escalations"},
    ],
      
          "product_project_management": [
        {"id": "product_management", "name": "Product Management"},
        {"id": "project_management", "name": "Project Management"},
        {"id": "program_management", "name": "Program Management"},
        {"id": "portfolio_pmo_management", "name": "Portfolio & PMO Management"},
        {"id": "agile_scrum_management", "name": "Agile & Scrum Management"},
        {"id": "product_operations_strategy", "name": "Product Operations & Strategy"},
    ],
          
       "healthcare_life_sciences": [
        {"id": "clinical_medical_practice", "name": "Clinical & Medical Practice"},
        {"id": "nursing_patient_care", "name": "Nursing & Patient Care"},
        {"id": "pharmacy_pharmaceutical_sciences", "name": "Pharmacy & Pharmaceutical Sciences"},
        {"id": "allied_health_rehabilitation", "name": "Allied Health & Rehabilitation"},
        {"id": "medical_laboratory_diagnostics", "name": "Medical Laboratory & Diagnostics"},
        {"id": "public_healthcare_administration", "name": "Public Health & Healthcare Administration"},
        {"id": "biotechnology_biomedical_research", "name": "Biotechnology & Biomedical Research"},
        {"id": "clinical_research_regulatory_affairs", "name": "Clinical Research & Regulatory Affairs"},
    ],
              
       "other_professional_roles": [
        {"id": "government_public_administration", "name": "Government & Public Administration"},
        {"id": "policy_international_development_ngos", "name": "Policy, International Development & NGOs"},
        {"id": "research_think_tanks_social_sciences", "name": "Research, Think Tanks & Social Sciences"},
        {"id": "environment_sustainability", "name": "Environment & Sustainability"},
        {"id": "agriculture_agribusiness", "name": "Agriculture & Agribusiness"},
        {"id": "real_estate_property_management", "name": "Real Estate & Property Management"},
        {"id": "security_defence_public_safety", "name": "Security, Defence & Public Safety"},
    ],
       
       "education_training": [
        {"id": "teaching_classroom_education", "name": "Teaching & Classroom Education"},
        {"id": "higher_education_university_administration", "name": "Higher Education & University Administration"},
        {"id": "corporate_training_learning_development", "name": "Corporate Training & Learning Development"},
        {"id": "instructional_design_elearning", "name": "Instructional Design & E-Learning"},
        {"id": "academic_research_educational_assessment", "name": "Academic Research & Educational Assessment"},
        {"id": "educational_leadership_administration", "name": "Educational Leadership & Administration"},
    ],
       
       "legal_compliance": [
        {"id": "legal_practice_advisory", "name": "Legal Practice & Advisory"},
        {"id": "corporate_commercial_law", "name": "Corporate & Commercial Law"},
        {"id": "regulatory_affairs_compliance", "name": "Regulatory Affairs & Compliance"},
        {"id": "governance_ethics_corporate_compliance", "name": "Governance, Ethics & Corporate Compliance"},
        {"id": "contracts_legal_operations", "name": "Contracts & Legal Operations"},
        {"id": "intellectual_property_privacy_law", "name": "Intellectual Property & Privacy Law"},
    ],
       
       "design_arts_creative": [
        {"id": "graphic_visual_design", "name": "Graphic & Visual Design"},
        {"id": "ui_ux_digital_product_design", "name": "UI/UX & Digital Product Design"},
        {"id": "animation_motion_graphics_3d", "name": "Animation, Motion Graphics & 3D"},
        {"id": "film_video_photography", "name": "Film, Video & Photography"},
        {"id": "writing_editing_publishing", "name": "Writing, Editing & Publishing"},
        {"id": "fashion_textile_interior_design", "name": "Fashion, Textile & Interior Design"},
        {"id": "fine_arts_illustration_creative_direction", "name": "Fine Arts, Illustration & Creative Direction"},
    ],
       
       "hospitality_retail_skilled_trades": [
        {"id": "hospitality_hotel_management", "name": "Hospitality & Hotel Management"},
        {"id": "food_beverage_services", "name": "Food & Beverage Services"},
        {"id": "travel_tourism_event_services", "name": "Travel, Tourism & Event Services"},
        {"id": "retail_store_operations", "name": "Retail & Store Operations"},
        {"id": "culinary_arts_food_production", "name": "Culinary Arts & Food Production"},
        {"id": "construction_building_trades", "name": "Construction & Building Trades"},
        {"id": "electrical_plumbing_mechanical_trades", "name": "Electrical, Plumbing & Mechanical Trades"},
        {"id": "automotive_repair_maintenance_services", "name": "Automotive, Repair & Maintenance Services"},
    ],
}



CANONICAL_ROLES = [
    {
        "id": "ai_engineer",
        "name": "AI Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Designs, develops, and deploys artificial intelligence systems and solutions.",
        "is_active": True,
    },
    {
        "id": "generative_ai_engineer",
        "name": "Generative AI Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Builds applications and systems powered by generative AI models for producing and transforming content.",
        "is_active": True,
    },
    {
        "id": "ai_application_developer",
        "name": "AI Application Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Develops software applications that incorporate AI capabilities into user-facing or business workflows.",
        "is_active": True,
    },
    {
        "id": "ai_solutions_engineer",
        "name": "AI Solutions Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Designs and implements AI-based solutions to address specific business and technical requirements.",
        "is_active": True,
    },
    {
        "id": "ai_architect",
        "name": "AI Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Defines the architecture and technical design of AI systems, including models, integrations, infrastructure, and deployment patterns.",
        "is_active": True,
    },
    {
        "id": "ai_research_engineer",
        "name": "AI Research Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Implements and evaluates AI research methods, prototypes, and experimental systems.",
        "is_active": True,
    },
    {
        "id": "ai_research_scientist",
        "name": "AI Research Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Conducts research into AI methods, algorithms, and models to advance artificial intelligence capabilities.",
        "is_active": True,
    },
    {
        "id": "llm_engineer",
        "name": "Large Language Model (LLM) Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Develops, adapts, evaluates, and optimizes applications and systems built around large language models.",
        "is_active": True,
    },
    {
        "id": "prompt_engineer",
        "name": "Prompt Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Designs, tests, and refines prompts and instructions to improve the reliability and quality of AI model outputs.",
        "is_active": True,
    },
    {
        "id": "conversational_ai_engineer",
        "name": "Conversational AI Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Builds AI-powered conversational systems such as chatbots and virtual assistants.",
        "is_active": True,
    },
    {
        "id": "ai_agent_developer",
        "name": "AI Agent Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Develops AI agents capable of using tools, performing tasks, and coordinating multi-step workflows.",
        "is_active": True,
    },
    {
        "id": "ai_integration_engineer",
        "name": "AI Integration Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Integrates AI models and services with existing applications, APIs, and enterprise systems.",
        "is_active": True,
    },
    {
        "id": "responsible_ai_engineer",
        "name": "Responsible AI Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Implements technical safeguards and evaluation practices addressing AI safety, fairness, transparency, and reliability.",
        "is_active": True,
    },
    {
        "id": "ai_platform_engineer",
        "name": "AI Platform Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "artificial_intelligence_generative_ai",
        "description": "Builds and maintains shared platforms and infrastructure for developing, deploying, and operating AI systems.",
        "is_active": True,
    },
]

CANONICAL_ROLES.extend([
    {
        "id": "machine_learning_engineer",
        "name": "Machine Learning Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Develops, trains, evaluates, and deploys machine learning models to solve practical problems.",
        "is_active": True,
    },
    {
        "id": "deep_learning_engineer",
        "name": "Deep Learning Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Builds and optimizes deep learning models and neural network architectures for complex tasks.",
        "is_active": True,
    },
    {
        "id": "applied_machine_learning_engineer",
        "name": "Applied Machine Learning Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Applies machine learning techniques to real-world products, applications, and business problems.",
        "is_active": True,
    },
    {
        "id": "machine_learning_research_engineer",
        "name": "Machine Learning Research Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Implements and experiments with machine learning algorithms, architectures, and research methods.",
        "is_active": True,
    },
    {
        "id": "machine_learning_research_scientist",
        "name": "Machine Learning Research Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Conducts research to develop new machine learning methods, algorithms, and model capabilities.",
        "is_active": True,
    },
    {
        "id": "computer_vision_engineer",
        "name": "Computer Vision Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Develops systems that interpret and analyze images, videos, and other visual data using machine learning.",
        "is_active": True,
    },
    {
        "id": "nlp_engineer",
        "name": "Natural Language Processing (NLP) Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Builds machine learning systems that process, understand, classify, and generate human language.",
        "is_active": True,
    },
    {
        "id": "reinforcement_learning_engineer",
        "name": "Reinforcement Learning Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Develops and trains models that learn through actions, feedback, and reward-based optimization.",
        "is_active": True,
    },
    {
        "id": "mlops_engineer",
        "name": "MLOps Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Automates machine learning workflows, including model training, deployment, monitoring, and lifecycle management.",
        "is_active": True,
    },
    {
        "id": "machine_learning_infrastructure_engineer",
        "name": "Machine Learning Infrastructure Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Builds and maintains the computing infrastructure required to train, serve, and operate machine learning models.",
        "is_active": True,
    },
    {
        "id": "machine_learning_platform_engineer",
        "name": "Machine Learning Platform Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Develops shared platforms, tools, and services that support machine learning development and deployment across teams.",
        "is_active": True,
    },
    {
        "id": "model_optimization_engineer",
        "name": "Model Optimization Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Improves model efficiency, performance, and resource usage through optimization, compression, and acceleration techniques.",
        "is_active": True,
    },
    {
        "id": "speech_recognition_engineer",
        "name": "Speech Recognition Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Develops machine learning systems that recognize, transcribe, and interpret spoken language.",
        "is_active": True,
    },
    {
        "id": "recommendation_systems_engineer",
        "name": "Recommendation Systems Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "machine_learning_deep_learning",
        "description": "Builds personalized recommendation and ranking systems for products, content, services, and other items.",
        "is_active": True,
    },
])

# ============================================================
# DATA SCIENCE & APPLIED AI
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "data_scientist",
        "name": "Data Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Analyzes complex data and develops statistical and machine learning models to generate insights and support decision-making.",
        "is_active": True,
    },
    {
        "id": "applied_scientist",
        "name": "Applied Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Applies scientific methods, statistical techniques, and machine learning to solve practical problems.",
        "is_active": True,
    },
    {
        "id": "research_data_scientist",
        "name": "Research Data Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Conducts data-driven research and develops analytical models to investigate complex problems and discover new insights.",
        "is_active": True,
    },
    {
        "id": "ai_scientist",
        "name": "AI Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Applies artificial intelligence research and scientific methods to develop and evaluate intelligent solutions.",
        "is_active": True,
    },
    {
        "id": "applied_ai_engineer",
        "name": "Applied AI Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Applies AI techniques and models to build practical solutions for real-world applications and business problems.",
        "is_active": True,
    },
    {
        "id": "data_science_engineer",
        "name": "Data Science Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Builds and maintains technical systems, pipelines, and tools that support data science workflows.",
        "is_active": True,
    },
    {
        "id": "predictive_modeling_scientist",
        "name": "Predictive Modeling Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Develops predictive models using statistical and machine learning techniques to forecast outcomes and trends.",
        "is_active": True,
    },
    {
        "id": "statistical_modeler",
        "name": "Statistical Modeler",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Builds and evaluates statistical models to identify patterns, explain relationships, and support data-driven decisions.",
        "is_active": True,
    },
    {
        "id": "computer_vision_scientist",
        "name": "Computer Vision Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Researches and develops scientific methods for extracting information and understanding visual data.",
        "is_active": True,
    },
    {
        "id": "nlp_scientist",
        "name": "NLP Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Researches and develops methods for analyzing, understanding, and generating human language using computational techniques.",
        "is_active": True,
    },
    {
        "id": "decision_scientist",
        "name": "Decision Scientist",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Uses statistical modeling, experimentation, and optimization to support strategic and operational decisions.",
        "is_active": True,
    },
    {
        "id": "quantitative_researcher",
        "name": "Quantitative Researcher",
        "professional_field_id": "technology_it",
        "subfield_id": "data_science_applied_ai",
        "description": "Develops mathematical and statistical models to analyze complex datasets and solve quantitative problems.",
        "is_active": True,
    },
])


# ============================================================
# SOFTWARE DEVELOPMENT
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "software_engineer",
        "name": "Software Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Designs, develops, tests, and maintains software systems and applications.",
        "is_active": True,
    },
    {
        "id": "software_developer",
        "name": "Software Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Develops and maintains software applications according to functional and technical requirements.",
        "is_active": True,
    },
    {
        "id": "application_developer",
        "name": "Application Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Builds and maintains software applications for business, desktop, and other computing environments.",
        "is_active": True,
    },
    {
        "id": "systems_software_engineer",
        "name": "Systems Software Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Develops and maintains system-level software, operating system components, and core computing services.",
        "is_active": True,
    },
    {
        "id": "desktop_application_developer",
        "name": "Desktop Application Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Develops and maintains software applications designed to run on desktop operating systems.",
        "is_active": True,
    },
    {
        "id": "api_developer",
        "name": "API Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Designs, develops, and maintains application programming interfaces that enable software systems to communicate.",
        "is_active": True,
    },
    {
        "id": "software_design_engineer",
        "name": "Software Design Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Designs software components and technical solutions, translating requirements into maintainable software architectures.",
        "is_active": True,
    },
    {
        "id": "embedded_software_developer",
        "name": "Embedded Software Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Develops software applications and system components that operate within embedded computing environments.",
        "is_active": True,
    },
    {
        "id": "game_developer",
        "name": "Game Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Develops and maintains interactive video games and their underlying software systems.",
        "is_active": True,
    },
    {
        "id": "distributed_systems_engineer",
        "name": "Distributed Systems Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Designs and develops software systems that coordinate processing and data across multiple interconnected machines.",
        "is_active": True,
    },
    {
        "id": "software_integration_engineer",
        "name": "Software Integration Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Integrates software components, applications, and services to ensure reliable communication and interoperability.",
        "is_active": True,
    },
    {
        "id": "software_consultant",
        "name": "Software Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "software_development",
        "description": "Advises organizations on software solutions and supports the design, implementation, and improvement of software systems.",
        "is_active": True,
    },
])


# ============================================================
# FRONTEND DEVELOPMENT
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "frontend_developer",
        "name": "Frontend Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Develops user-facing web interfaces and implements interactive functionality for websites and applications.",
        "is_active": True,
    },
    {
        "id": "frontend_engineer",
        "name": "Frontend Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Engineers scalable, performant, and maintainable frontend applications and user interfaces.",
        "is_active": True,
    },
    {
        "id": "react_developer",
        "name": "React Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Develops interactive web applications and user interfaces using the React library.",
        "is_active": True,
    },
    {
        "id": "angular_developer",
        "name": "Angular Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Builds and maintains web applications and user interfaces using the Angular framework.",
        "is_active": True,
    },
    {
        "id": "vuejs_developer",
        "name": "Vue.js Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Develops web interfaces and applications using the Vue.js framework.",
        "is_active": True,
    },
    {
        "id": "javascript_developer",
        "name": "JavaScript Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Develops interactive web applications and frontend functionality using JavaScript.",
        "is_active": True,
    },
    {
        "id": "typescript_developer",
        "name": "TypeScript Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Develops maintainable web applications and frontend systems using TypeScript.",
        "is_active": True,
    },
    {
        "id": "ui_developer",
        "name": "UI Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Implements user interface designs and develops responsive, accessible web interface components.",
        "is_active": True,
    },
    {
        "id": "web_ui_engineer",
        "name": "Web UI Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Engineers reusable, responsive, and high-performance user interface systems for web applications.",
        "is_active": True,
    },
    {
        "id": "frontend_architect",
        "name": "Frontend Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "frontend_development",
        "description": "Defines frontend architecture, technical standards, and design patterns for scalable web applications.",
        "is_active": True,
    },
])



# ============================================================
# BACKEND DEVELOPMENT
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "backend_developer",
        "name": "Backend Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Develops and maintains server-side application logic, APIs, databases, and backend services.",
        "is_active": True,
    },
    {
        "id": "backend_engineer",
        "name": "Backend Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Engineers scalable, reliable, and secure backend systems and services.",
        "is_active": True,
    },
    {
        "id": "python_developer",
        "name": "Python Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Develops server-side applications, APIs, and backend services using Python.",
        "is_active": True,
    },
    {
        "id": "java_developer",
        "name": "Java Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Builds enterprise backend applications and services using Java.",
        "is_active": True,
    },
    {
        "id": "nodejs_developer",
        "name": "Node.js Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Develops server-side applications, APIs, and services using Node.js.",
        "is_active": True,
    },
    {
        "id": "dotnet_developer",
        "name": ".NET Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Develops backend applications, APIs, and enterprise services using the .NET ecosystem.",
        "is_active": True,
    },
    {
        "id": "php_developer",
        "name": "PHP Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Builds and maintains server-side applications and APIs using PHP.",
        "is_active": True,
    },
    {
        "id": "go_developer",
        "name": "Go Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Develops performant backend services and distributed applications using Go.",
        "is_active": True,
    },
    {
        "id": "api_engineer",
        "name": "API Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Designs, builds, and maintains APIs that enable communication between software systems.",
        "is_active": True,
    },
    {
        "id": "microservices_engineer",
        "name": "Microservices Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Designs and develops distributed applications using independently deployable microservices.",
        "is_active": True,
    },
    {
        "id": "backend_architect",
        "name": "Backend Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "backend_development",
        "description": "Defines backend system architecture, integration patterns, scalability, and technical standards.",
        "is_active": True,
    },
])


# ============================================================
# FULL STACK DEVELOPMENT
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "full_stack_developer",
        "name": "Full Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Develops both frontend and backend components of complete software applications.",
        "is_active": True,
    },
    {
        "id": "full_stack_engineer",
        "name": "Full Stack Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Engineers end-to-end application systems spanning user interfaces, backend services, and integrations.",
        "is_active": True,
    },
    {
        "id": "mern_stack_developer",
        "name": "MERN Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Builds full stack web applications using MongoDB, Express.js, React, and Node.js.",
        "is_active": True,
    },
    {
        "id": "mean_stack_developer",
        "name": "MEAN Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Develops full stack web applications using MongoDB, Express.js, Angular, and Node.js.",
        "is_active": True,
    },
    {
        "id": "java_full_stack_developer",
        "name": "Java Full Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Develops end-to-end applications using Java-based backend technologies and frontend frameworks.",
        "is_active": True,
    },
    {
        "id": "python_full_stack_developer",
        "name": "Python Full Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Builds complete web applications using Python backend technologies and frontend frameworks.",
        "is_active": True,
    },
    {
        "id": "dotnet_full_stack_developer",
        "name": ".NET Full Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Develops end-to-end applications using .NET backend technologies and modern frontend frameworks.",
        "is_active": True,
    },
    {
        "id": "php_full_stack_developer",
        "name": "PHP Full Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Develops complete web applications using PHP backend technologies and frontend tools.",
        "is_active": True,
    },
    {
        "id": "javascript_full_stack_developer",
        "name": "JavaScript Full Stack Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Builds end-to-end web applications using JavaScript across frontend and backend environments.",
        "is_active": True,
    },
    {
        "id": "full_stack_architect",
        "name": "Full Stack Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "full_stack_development",
        "description": "Defines end-to-end application architecture, technology choices, and integration strategies.",
        "is_active": True,
    },
])


# ============================================================
# MOBILE APPLICATION DEVELOPMENT
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "mobile_application_developer",
        "name": "Mobile Application Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Develops and maintains applications for smartphones and other mobile devices.",
        "is_active": True,
    },
    {
        "id": "mobile_application_engineer",
        "name": "Mobile Application Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Engineers scalable, performant, and reliable mobile application systems.",
        "is_active": True,
    },
    {
        "id": "android_developer",
        "name": "Android Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Develops and maintains applications for Android devices.",
        "is_active": True,
    },
    {
        "id": "ios_developer",
        "name": "iOS Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Develops and maintains applications for Apple's iOS platform.",
        "is_active": True,
    },
    {
        "id": "react_native_developer",
        "name": "React Native Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Builds cross-platform mobile applications using React Native.",
        "is_active": True,
    },
    {
        "id": "flutter_developer",
        "name": "Flutter Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Develops cross-platform mobile applications using Flutter.",
        "is_active": True,
    },
    {
        "id": "kotlin_developer",
        "name": "Kotlin Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Develops mobile applications and Android software using Kotlin.",
        "is_active": True,
    },
    {
        "id": "swift_developer",
        "name": "Swift Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Develops applications for Apple platforms using the Swift programming language.",
        "is_active": True,
    },
    {
        "id": "cross_platform_mobile_developer",
        "name": "Cross-Platform Mobile Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Builds mobile applications that operate across multiple platforms using shared codebases.",
        "is_active": True,
    },
    {
        "id": "mobile_application_architect",
        "name": "Mobile Application Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "mobile_application_development",
        "description": "Defines mobile application architecture, technical standards, and platform integration strategies.",
        "is_active": True,
    },
])


# ============================================================
# WEB DEVELOPMENT
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "web_developer",
        "name": "Web Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Develops and maintains websites and web-based applications.",
        "is_active": True,
    },
    {
        "id": "web_engineer",
        "name": "Web Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Engineers reliable, scalable, and performant web systems and applications.",
        "is_active": True,
    },
    {
        "id": "wordpress_developer",
        "name": "WordPress Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Develops and customizes websites, themes, and plugins using WordPress.",
        "is_active": True,
    },
    {
        "id": "cms_developer",
        "name": "CMS Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Develops and customizes content management systems and related web solutions.",
        "is_active": True,
    },
    {
        "id": "ecommerce_developer",
        "name": "E-commerce Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Builds and maintains online commerce websites, storefronts, and shopping functionality.",
        "is_active": True,
    },
    {
        "id": "web_application_developer",
        "name": "Web Application Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Develops interactive browser-based applications and web software solutions.",
        "is_active": True,
    },
    {
        "id": "web_designer_developer",
        "name": "Web Designer & Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Combines visual website design with the development and implementation of web pages.",
        "is_active": True,
    },
    {
        "id": "web_performance_engineer",
        "name": "Web Performance Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Improves website speed, responsiveness, loading performance, and runtime efficiency.",
        "is_active": True,
    },
    {
        "id": "web_accessibility_engineer",
        "name": "Web Accessibility Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Ensures websites and web applications meet accessibility standards and support inclusive user experiences.",
        "is_active": True,
    },
    {
        "id": "web_architect",
        "name": "Web Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "web_development",
        "description": "Defines the architecture, technical structure, and integration patterns of web platforms.",
        "is_active": True,
    },
])


# ============================================================
# CLOUD COMPUTING & ARCHITECTURE
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "cloud_engineer",
        "name": "Cloud Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Builds, deploys, and maintains cloud-based infrastructure, services, and applications.",
        "is_active": True,
    },
    {
        "id": "cloud_architect",
        "name": "Cloud Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Designs cloud architecture, infrastructure strategies, and scalable cloud environments.",
        "is_active": True,
    },
    {
        "id": "cloud_solutions_architect",
        "name": "Cloud Solutions Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Designs cloud-based technical solutions aligned with business and application requirements.",
        "is_active": True,
    },
    {
        "id": "cloud_infrastructure_engineer",
        "name": "Cloud Infrastructure Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Builds and manages cloud infrastructure, computing resources, storage, and networking environments.",
        "is_active": True,
    },
    {
        "id": "cloud_platform_engineer",
        "name": "Cloud Platform Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Develops and maintains cloud platforms and shared services supporting application deployment and operations.",
        "is_active": True,
    },
    {
        "id": "aws_cloud_engineer",
        "name": "AWS Cloud Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Builds and manages cloud infrastructure and services using Amazon Web Services.",
        "is_active": True,
    },
    {
        "id": "azure_cloud_engineer",
        "name": "Azure Cloud Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Builds and manages cloud infrastructure and services using Microsoft Azure.",
        "is_active": True,
    },
    {
        "id": "google_cloud_engineer",
        "name": "Google Cloud Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Builds and manages cloud infrastructure and services using Google Cloud.",
        "is_active": True,
    },
    {
        "id": "cloud_security_engineer",
        "name": "Cloud Security Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Implements security controls and safeguards to protect cloud infrastructure, services, and workloads.",
        "is_active": True,
    },
    {
        "id": "cloud_network_engineer",
        "name": "Cloud Network Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Designs and manages cloud networking, connectivity, routing, and network security configurations.",
        "is_active": True,
    },
    {
        "id": "cloud_operations_engineer",
        "name": "Cloud Operations Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Monitors and maintains cloud environments, ensuring availability, reliability, and operational efficiency.",
        "is_active": True,
    },
    {
        "id": "cloud_migration_engineer",
        "name": "Cloud Migration Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cloud_computing_architecture",
        "description": "Plans and executes migrations of applications, infrastructure, and data to cloud environments.",
        "is_active": True,
    },
])


# ============================================================
# DEVOPS & SITE RELIABILITY ENGINEERING
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "devops_engineer",
        "name": "DevOps Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Automates software development, deployment, infrastructure, and operational workflows.",
        "is_active": True,
    },
    {
        "id": "site_reliability_engineer",
        "name": "Site Reliability Engineer (SRE)",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Improves system reliability, availability, performance, and resilience through engineering practices.",
        "is_active": True,
    },
    {
        "id": "platform_engineer",
        "name": "Platform Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Builds internal developer platforms, infrastructure tools, and services that improve software delivery.",
        "is_active": True,
    },
    {
        "id": "build_release_engineer",
        "name": "Build and Release Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Manages software build systems, release processes, and automated delivery pipelines.",
        "is_active": True,
    },
    {
        "id": "cicd_engineer",
        "name": "CI/CD Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Designs and maintains continuous integration and continuous delivery pipelines for software systems.",
        "is_active": True,
    },
    {
        "id": "infrastructure_automation_engineer",
        "name": "Infrastructure Automation Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Automates infrastructure provisioning, configuration, deployment, and management processes.",
        "is_active": True,
    },
    {
        "id": "devsecops_engineer",
        "name": "DevSecOps Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Integrates security practices and automated security controls throughout software delivery pipelines.",
        "is_active": True,
    },
    {
        "id": "kubernetes_engineer",
        "name": "Kubernetes Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Deploys and manages containerized applications and infrastructure using Kubernetes.",
        "is_active": True,
    },
    {
        "id": "containerization_engineer",
        "name": "Containerization Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Designs and manages containerized application environments and container orchestration solutions.",
        "is_active": True,
    },
    {
        "id": "observability_engineer",
        "name": "Observability Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Builds monitoring, logging, tracing, and observability systems for distributed applications.",
        "is_active": True,
    },
    {
        "id": "release_engineer",
        "name": "Release Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Coordinates and automates software release processes, deployment readiness, and version management.",
        "is_active": True,
    },
    {
        "id": "devops_architect",
        "name": "DevOps Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "devops_site_reliability_engineering",
        "description": "Defines DevOps architecture, automation strategies, delivery standards, and infrastructure practices.",
        "is_active": True,
    },
])


# ============================================================
# CYBERSECURITY & INFORMATION SECURITY
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "cybersecurity_engineer",
        "name": "Cybersecurity Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Develops and implements technical security solutions to protect systems, networks, and data.",
        "is_active": True,
    },
    {
        "id": "information_security_analyst",
        "name": "Information Security Analyst",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Analyzes security risks, monitors threats, and helps protect organizational information assets.",
        "is_active": True,
    },
    {
        "id": "security_engineer",
        "name": "Security Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Designs, implements, and maintains security technologies and controls across IT systems.",
        "is_active": True,
    },
    {
        "id": "security_architect",
        "name": "Security Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Designs security architecture, policies, and technical controls to protect enterprise systems.",
        "is_active": True,
    },
    {
        "id": "application_security_engineer",
        "name": "Application Security Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Identifies and mitigates software vulnerabilities and integrates security into application development.",
        "is_active": True,
    },
    {
        "id": "cloud_security_architect",
        "name": "Cloud Security Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Designs security architecture and controls for cloud platforms, infrastructure, and workloads.",
        "is_active": True,
    },
    {
        "id": "penetration_tester",
        "name": "Penetration Tester",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Performs authorized security testing to identify and validate vulnerabilities in systems and applications.",
        "is_active": True,
    },
    {
        "id": "soc_analyst",
        "name": "Security Operations Center (SOC) Analyst",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Monitors security alerts, investigates suspicious activity, and supports cybersecurity incident detection.",
        "is_active": True,
    },
    {
        "id": "incident_response_engineer",
        "name": "Incident Response Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Investigates and responds to security incidents while coordinating containment and recovery activities.",
        "is_active": True,
    },
    {
        "id": "digital_forensics_analyst",
        "name": "Digital Forensics Analyst",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Examines digital evidence and analyzes electronic systems to investigate security incidents.",
        "is_active": True,
    },
    {
        "id": "identity_access_management_engineer",
        "name": "Identity and Access Management Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Designs and manages identity, authentication, authorization, and access control systems.",
        "is_active": True,
    },
    {
        "id": "vulnerability_management_engineer",
        "name": "Vulnerability Management Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Identifies, assesses, prioritizes, and coordinates remediation of security vulnerabilities.",
        "is_active": True,
    },
    {
        "id": "grc_analyst",
        "name": "Governance, Risk and Compliance (GRC) Analyst",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Assesses technology risks and supports information security governance, controls, and compliance requirements.",
        "is_active": True,
    },
    {
        "id": "security_consultant",
        "name": "Security Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "cybersecurity_information_security",
        "description": "Advises organizations on cybersecurity risks, security controls, and information protection strategies.",
        "is_active": True,
    },
])


# ============================================================
# NETWORKING & INFRASTRUCTURE
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "network_engineer",
        "name": "Network Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Designs, implements, and maintains computer networks and network connectivity.",
        "is_active": True,
    },
    {
        "id": "network_administrator",
        "name": "Network Administrator",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Manages network infrastructure, configurations, access, and day-to-day network operations.",
        "is_active": True,
    },
    {
        "id": "network_architect",
        "name": "Network Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Designs enterprise network architecture, connectivity strategies, and network infrastructure standards.",
        "is_active": True,
    },
    {
        "id": "systems_administrator",
        "name": "Systems Administrator",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Maintains servers, operating systems, user accounts, and core IT infrastructure.",
        "is_active": True,
    },
    {
        "id": "systems_engineer",
        "name": "Systems Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Designs, integrates, and maintains interconnected computing systems and infrastructure.",
        "is_active": True,
    },
    {
        "id": "infrastructure_engineer",
        "name": "Infrastructure Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Builds and maintains IT infrastructure, including servers, networks, storage, and computing environments.",
        "is_active": True,
    },
    {
        "id": "network_security_engineer",
        "name": "Network Security Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Implements and maintains security controls that protect network infrastructure and communications.",
        "is_active": True,
    },
    {
        "id": "noc_engineer",
        "name": "Network Operations Center (NOC) Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Monitors network infrastructure, troubleshoots connectivity issues, and supports network availability.",
        "is_active": True,
    },
    {
        "id": "wireless_network_engineer",
        "name": "Wireless Network Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Designs and maintains wireless networks, Wi-Fi infrastructure, and radio connectivity systems.",
        "is_active": True,
    },
    {
        "id": "telecommunications_engineer",
        "name": "Telecommunications Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Designs and maintains telecommunications networks, transmission systems, and communication infrastructure.",
        "is_active": True,
    },
    {
        "id": "data_center_engineer",
        "name": "Data Center Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Maintains data center infrastructure, including servers, storage, connectivity, and hardware systems.",
        "is_active": True,
    },
    {
        "id": "infrastructure_architect",
        "name": "Infrastructure Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "networking_infrastructure",
        "description": "Defines enterprise IT infrastructure architecture, technology standards, and infrastructure integration strategies.",
        "is_active": True,
    },
])



# ============================================================
# DATABASE & DATA ADMINISTRATION — 12 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "database_administrator",
        "name": "Database Administrator",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Manages database systems, availability, maintenance, backups, and performance.",
        "is_active": True,
    },
    {
        "id": "database_engineer",
        "name": "Database Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Designs, builds, and maintains database infrastructure and data storage systems.",
        "is_active": True,
    },
    {
        "id": "database_developer",
        "name": "Database Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Develops database structures, queries, procedures, and data-driven applications.",
        "is_active": True,
    },
    {
        "id": "database_architect",
        "name": "Database Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Designs database architecture, data models, and scalable storage solutions.",
        "is_active": True,
    },
    {
        "id": "sql_developer",
        "name": "SQL Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Develops and optimizes SQL queries, stored procedures, and relational database solutions.",
        "is_active": True,
    },
    {
        "id": "data_architect",
        "name": "Data Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Designs enterprise data structures, models, and data management architectures.",
        "is_active": True,
    },
    {
        "id": "database_reliability_engineer",
        "name": "Database Reliability Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Ensures database reliability, availability, resilience, and operational performance.",
        "is_active": True,
    },
    {
        "id": "nosql_database_engineer",
        "name": "NoSQL Database Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Builds and manages non-relational database systems and distributed data stores.",
        "is_active": True,
    },
    {
        "id": "database_performance_engineer",
        "name": "Database Performance Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Analyzes and improves database performance, query efficiency, and resource utilization.",
        "is_active": True,
    },
    {
        "id": "data_migration_engineer",
        "name": "Data Migration Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Plans and executes database and data migrations between systems and platforms.",
        "is_active": True,
    },
    {
        "id": "database_security_engineer",
        "name": "Database Security Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Protects database systems through access controls, encryption, and security monitoring.",
        "is_active": True,
    },
    {
        "id": "database_operations_engineer",
        "name": "Database Operations Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "database_data_administration",
        "description": "Maintains database operations, monitoring, deployments, and operational support.",
        "is_active": True,
    },
])


# ============================================================
# SOFTWARE TESTING & QUALITY ASSURANCE — 12 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "software_test_engineer",
        "name": "Software Test Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Tests software applications to identify defects and verify functional requirements.",
        "is_active": True,
    },
    {
        "id": "qa_engineer",
        "name": "QA Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Ensures software quality through testing processes, defect tracking, and validation.",
        "is_active": True,
    },
    {
        "id": "automation_test_engineer",
        "name": "Automation Test Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Develops automated test scripts and frameworks for software quality verification.",
        "is_active": True,
    },
    {
        "id": "manual_test_engineer",
        "name": "Manual Test Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Performs manual software testing to identify defects and validate application behavior.",
        "is_active": True,
    },
    {
        "id": "sdet",
        "name": "Software Development Engineer in Test (SDET)",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Combines software development and testing to build scalable automated testing solutions.",
        "is_active": True,
    },
    {
        "id": "performance_test_engineer",
        "name": "Performance Test Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Evaluates application speed, scalability, stability, and performance under varying workloads.",
        "is_active": True,
    },
    {
        "id": "api_test_engineer",
        "name": "API Test Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Tests API functionality, reliability, integration, and performance.",
        "is_active": True,
    },
    {
        "id": "quality_assurance_analyst",
        "name": "Quality Assurance Analyst",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Analyzes software quality requirements, testing results, and defect reports.",
        "is_active": True,
    },
    {
        "id": "test_lead",
        "name": "Test Lead",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Leads testing teams, coordinates test execution, and oversees quality activities.",
        "is_active": True,
    },
    {
        "id": "qa_manager",
        "name": "QA Manager",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Manages quality assurance teams, testing strategies, and software quality processes.",
        "is_active": True,
    },
    {
        "id": "security_test_engineer",
        "name": "Security Test Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Tests applications for security vulnerabilities and validates security controls.",
        "is_active": True,
    },
    {
        "id": "test_automation_architect",
        "name": "Test Automation Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "software_testing_quality_assurance",
        "description": "Designs enterprise test automation frameworks, standards, and architectures.",
        "is_active": True,
    },
])


# ============================================================
# EMBEDDED SYSTEMS & FIRMWARE — 12 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "embedded_systems_engineer",
        "name": "Embedded Systems Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops embedded computing systems for electronic and connected devices.",
        "is_active": True,
    },
    {
        "id": "embedded_software_engineer",
        "name": "Embedded Software Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops software that operates within embedded hardware platforms.",
        "is_active": True,
    },
    {
        "id": "firmware_engineer",
        "name": "Firmware Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops and maintains low-level firmware for electronic devices and hardware.",
        "is_active": True,
    },
    {
        "id": "embedded_c_cpp_developer",
        "name": "Embedded C/C++ Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops embedded applications and device software using C and C++.",
        "is_active": True,
    },
    {
        "id": "embedded_linux_engineer",
        "name": "Embedded Linux Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Builds and maintains Linux-based software environments for embedded devices.",
        "is_active": True,
    },
    {
        "id": "rtos_engineer",
        "name": "RTOS Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops real-time operating system software for embedded and time-critical systems.",
        "is_active": True,
    },
    {
        "id": "iot_engineer",
        "name": "IoT Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops connected device solutions involving embedded systems and IoT platforms.",
        "is_active": True,
    },
    {
        "id": "embedded_hardware_software_integration_engineer",
        "name": "Embedded Hardware-Software Integration Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Integrates embedded software with hardware components and validates system behavior.",
        "is_active": True,
    },
    {
        "id": "firmware_developer",
        "name": "Firmware Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Programs and maintains firmware for microcontrollers and electronic devices.",
        "is_active": True,
    },
    {
        "id": "embedded_systems_architect",
        "name": "Embedded Systems Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Designs embedded system architectures and hardware-software integration strategies.",
        "is_active": True,
    },
    {
        "id": "automotive_embedded_software_engineer",
        "name": "Automotive Embedded Software Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops embedded software for automotive electronic control systems.",
        "is_active": True,
    },
    {
        "id": "robotics_software_engineer",
        "name": "Robotics Software Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "embedded_systems_firmware",
        "description": "Develops software and control systems for robotic devices and embedded platforms.",
        "is_active": True,
    },
])


# ============================================================
# HARDWARE & SEMICONDUCTOR ENGINEERING — 12 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "hardware_engineer",
        "name": "Hardware Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Designs, develops, and tests electronic hardware systems and components.",
        "is_active": True,
    },
    {
        "id": "semiconductor_engineer",
        "name": "Semiconductor Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Works on semiconductor devices, fabrication processes, and chip technologies.",
        "is_active": True,
    },
    {
        "id": "vlsi_design_engineer",
        "name": "VLSI Design Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Designs very-large-scale integrated circuits and digital hardware architectures.",
        "is_active": True,
    },
    {
        "id": "asic_design_engineer",
        "name": "ASIC Design Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Designs application-specific integrated circuits for specialized hardware applications.",
        "is_active": True,
    },
    {
        "id": "fpga_design_engineer",
        "name": "FPGA Design Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Develops and validates digital logic designs using field-programmable gate arrays.",
        "is_active": True,
    },
    {
        "id": "pcb_design_engineer",
        "name": "PCB Design Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Designs printed circuit boards, layouts, and electronic hardware assemblies.",
        "is_active": True,
    },
    {
        "id": "chip_design_engineer",
        "name": "Chip Design Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Designs and develops integrated circuit and semiconductor chip components.",
        "is_active": True,
    },
    {
        "id": "verification_engineer",
        "name": "Verification Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Verifies hardware designs through simulation, validation, and functional testing.",
        "is_active": True,
    },
    {
        "id": "physical_design_engineer",
        "name": "Physical Design Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Implements and optimizes physical layouts of integrated circuit designs.",
        "is_active": True,
    },
    {
        "id": "hardware_validation_engineer",
        "name": "Hardware Validation Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Validates electronic hardware functionality, reliability, and design requirements.",
        "is_active": True,
    },
    {
        "id": "hardware_architect",
        "name": "Hardware Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "hardware_semiconductor_engineering",
        "description": "Defines hardware system architecture, component selection, and technical design standards.",
        "is_active": True,
    },
])


# ============================================================
# ENTERPRISE APPLICATIONS & ERP — 14 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "erp_consultant",
        "name": "ERP Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Advises organizations on enterprise resource planning systems and implementations.",
        "is_active": True,
    },
    {
        "id": "erp_developer",
        "name": "ERP Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Develops and customizes enterprise resource planning applications and integrations.",
        "is_active": True,
    },
    {
        "id": "sap_consultant",
        "name": "SAP Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Implements, configures, and supports SAP enterprise business applications.",
        "is_active": True,
    },
    {
        "id": "sap_developer",
        "name": "SAP Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Develops and customizes SAP applications, extensions, and integrations.",
        "is_active": True,
    },
    {
        "id": "salesforce_developer",
        "name": "Salesforce Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Builds and customizes Salesforce applications, workflows, and platform integrations.",
        "is_active": True,
    },
    {
        "id": "oracle_applications_consultant",
        "name": "Oracle Applications Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Implements and supports Oracle enterprise applications and business systems.",
        "is_active": True,
    },
    {
        "id": "microsoft_dynamics_consultant",
        "name": "Microsoft Dynamics Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Implements and configures Microsoft Dynamics business applications.",
        "is_active": True,
    },
    {
        "id": "enterprise_applications_developer",
        "name": "Enterprise Applications Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Develops and integrates enterprise business applications and software solutions.",
        "is_active": True,
    },
    {
        "id": "enterprise_solutions_architect",
        "name": "Enterprise Solutions Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Designs enterprise application architectures and integrated business technology solutions.",
        "is_active": True,
    },
    {
        "id": "erp_functional_consultant",
        "name": "ERP Functional Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Maps business processes to ERP modules and configures functional requirements.",
        "is_active": True,
    },
    {
        "id": "erp_technical_consultant",
        "name": "ERP Technical Consultant",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Handles ERP customizations, technical integrations, and application development.",
        "is_active": True,
    },
    {
        "id": "crm_developer",
        "name": "CRM Developer",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Develops and customizes customer relationship management applications and integrations.",
        "is_active": True,
    },
    {
        "id": "enterprise_applications_administrator",
        "name": "Enterprise Applications Administrator",
        "professional_field_id": "technology_it",
        "subfield_id": "enterprise_applications_erp",
        "description": "Administers enterprise applications, user access, configurations, and system operations.",
        "is_active": True,
    },
])


# ============================================================
# IT SUPPORT & TECHNICAL SERVICES — 12 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "it_support_specialist",
        "name": "IT Support Specialist",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Provides technical assistance and troubleshooting for users, devices, and IT systems.",
        "is_active": True,
    },
    {
        "id": "it_support_engineer",
        "name": "IT Support Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Maintains IT systems and resolves hardware, software, and infrastructure issues.",
        "is_active": True,
    },
    {
        "id": "technical_support_engineer",
        "name": "Technical Support Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Diagnoses and resolves technical issues involving software, hardware, and technology products.",
        "is_active": True,
    },
    {
        "id": "desktop_support_engineer",
        "name": "Desktop Support Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Supports desktop computers, operating systems, peripherals, and end-user environments.",
        "is_active": True,
    },
    {
        "id": "help_desk_analyst",
        "name": "Help Desk Analyst",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Handles user support requests, service tickets, and routine technical troubleshooting.",
        "is_active": True,
    },
    {
        "id": "it_service_desk_analyst",
        "name": "IT Service Desk Analyst",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Manages IT service desk requests and coordinates incident resolution.",
        "is_active": True,
    },
    {
        "id": "systems_support_engineer",
        "name": "Systems Support Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Provides operational support and troubleshooting for enterprise systems and platforms.",
        "is_active": True,
    },
    {
        "id": "application_support_engineer",
        "name": "Application Support Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Supports business applications by investigating incidents and resolving application issues.",
        "is_active": True,
    },
    {
        "id": "it_field_support_engineer",
        "name": "IT Field Support Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Provides on-site installation, maintenance, and technical support for IT equipment.",
        "is_active": True,
    },
    {
        "id": "it_operations_support_engineer",
        "name": "IT Operations Support Engineer",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Supports daily IT operations, system monitoring, incident handling, and service continuity.",
        "is_active": True,
    },
    {
        "id": "technical_support_specialist",
        "name": "Technical Support Specialist",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Assists customers and users with technical product issues and troubleshooting.",
        "is_active": True,
    },
    {
        "id": "it_support_manager",
        "name": "IT Support Manager",
        "professional_field_id": "technology_it",
        "subfield_id": "it_support_technical_services",
        "description": "Leads IT support teams, service delivery, and end-user technical support operations.",
        "is_active": True,
    },
])


# ============================================================
# IT MANAGEMENT & ARCHITECTURE — 12 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "it_manager",
        "name": "IT Manager",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Manages IT teams, technology operations, infrastructure, and organizational IT services.",
        "is_active": True,
    },
    {
        "id": "it_director",
        "name": "IT Director",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Directs enterprise IT functions, technology investments, and operational strategy.",
        "is_active": True,
    },
    {
        "id": "chief_information_officer",
        "name": "Chief Information Officer (CIO)",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Leads organizational information technology strategy, governance, and information systems.",
        "is_active": True,
    },
    {
        "id": "chief_technology_officer",
        "name": "Chief Technology Officer (CTO)",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Defines technology vision, engineering direction, and technical innovation strategy.",
        "is_active": True,
    },
    {
        "id": "it_architect",
        "name": "IT Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Designs IT systems and technology architectures aligned with business requirements.",
        "is_active": True,
    },
    {
        "id": "enterprise_architect",
        "name": "Enterprise Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Defines enterprise-wide technology architecture, standards, and system integration strategies.",
        "is_active": True,
    },
    {
        "id": "solutions_architect",
        "name": "Solutions Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Designs end-to-end technical solutions to meet business and system requirements.",
        "is_active": True,
    },
    {
        "id": "technical_architect",
        "name": "Technical Architect",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Defines technical designs, application structures, and implementation standards.",
        "is_active": True,
    },
    {
        "id": "it_governance_manager",
        "name": "IT Governance Manager",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Oversees IT governance frameworks, policies, controls, and compliance.",
        "is_active": True,
    },
    {
        "id": "it_service_management_manager",
        "name": "IT Service Management Manager",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Manages IT service management processes, service quality, and delivery performance.",
        "is_active": True,
    },
    {
        "id": "technology_strategy_manager",
        "name": "Technology Strategy Manager",
        "professional_field_id": "technology_it",
        "subfield_id": "it_management_architecture",
        "description": "Develops technology strategies and roadmaps aligned with organizational goals.",
        "is_active": True,
    },
])


# ============================================================
# DATA ANALYSIS & REPORTING — 10 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "data_analyst",
        "name": "Data Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Analyzes datasets to identify trends, generate insights, and support business decisions.",
        "is_active": True,
    },
    {
        "id": "senior_data_analyst",
        "name": "Senior Data Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Leads complex data analysis and translates findings into actionable business insights.",
        "is_active": True,
    },
    {
        "id": "reporting_analyst",
        "name": "Reporting Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Creates, maintains, and analyzes operational and business performance reports.",
        "is_active": True,
    },
    {
        "id": "mis_analyst",
        "name": "MIS Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Manages management information systems and prepares business performance reports.",
        "is_active": True,
    },
    {
        "id": "data_reporting_specialist",
        "name": "Data Reporting Specialist",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Produces structured data reports and maintains reporting processes and datasets.",
        "is_active": True,
    },
    {
        "id": "business_data_analyst",
        "name": "Business Data Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Analyzes business data to evaluate performance and support operational decisions.",
        "is_active": True,
    },
    {
        "id": "operations_data_analyst",
        "name": "Operations Data Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Analyzes operational datasets to identify process trends and improvement opportunities.",
        "is_active": True,
    },
    {
        "id": "data_quality_analyst",
        "name": "Data Quality Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Evaluates data accuracy, consistency, completeness, and quality standards.",
        "is_active": True,
    },
    {
        "id": "data_visualization_analyst",
        "name": "Data Visualization Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Transforms analytical findings into clear charts, dashboards, and visual reports.",
        "is_active": True,
    },
    {
        "id": "data_analysis_manager",
        "name": "Data Analysis Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_analysis_reporting",
        "description": "Leads data analysis teams and oversees analytical reporting and insight generation.",
        "is_active": True,
    },
])


# ============================================================
# BUSINESS INTELLIGENCE & VISUALIZATION — 10 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "business_intelligence_analyst",
        "name": "Business Intelligence Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Analyzes business information and develops insights through BI tools and reporting.",
        "is_active": True,
    },
    {
        "id": "business_intelligence_developer",
        "name": "Business Intelligence Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Builds BI solutions, data models, dashboards, and reporting applications.",
        "is_active": True,
    },
    {
        "id": "bi_engineer",
        "name": "BI Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Develops and maintains business intelligence systems, pipelines, and reporting infrastructure.",
        "is_active": True,
    },
    {
        "id": "bi_consultant",
        "name": "BI Consultant",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Advises organizations on BI platforms, reporting solutions, and analytics implementation.",
        "is_active": True,
    },
    {
        "id": "power_bi_developer",
        "name": "Power BI Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Creates Power BI dashboards, data models, reports, and business analytics solutions.",
        "is_active": True,
    },
    {
        "id": "tableau_developer",
        "name": "Tableau Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Builds Tableau dashboards and interactive visualizations for business reporting.",
        "is_active": True,
    },
    {
        "id": "data_visualization_developer",
        "name": "Data Visualization Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Develops interactive data visualizations and visual analytics applications.",
        "is_active": True,
    },
    {
        "id": "business_intelligence_architect",
        "name": "Business Intelligence Architect",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Designs BI architectures, semantic models, and enterprise reporting solutions.",
        "is_active": True,
    },
    {
        "id": "bi_reporting_analyst",
        "name": "BI Reporting Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Develops and maintains business intelligence reports and analytical dashboards.",
        "is_active": True,
    },
    {
        "id": "business_intelligence_manager",
        "name": "Business Intelligence Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_intelligence_visualization",
        "description": "Leads BI teams, reporting strategy, dashboard development, and analytics delivery.",
        "is_active": True,
    },
])



# ============================================================
# DATA ENGINEERING — 12 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "data_engineer",
        "name": "Data Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Builds and maintains data pipelines, infrastructure, and systems for processing and delivering data.",
        "is_active": True,
    },
    {
        "id": "senior_data_engineer",
        "name": "Senior Data Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Leads the design and development of scalable data engineering solutions and pipelines.",
        "is_active": True,
    },
    {
        "id": "etl_developer",
        "name": "ETL Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Develops extraction, transformation, and loading processes for data integration.",
        "is_active": True,
    },
    {
        "id": "data_pipeline_engineer",
        "name": "Data Pipeline Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Builds and maintains reliable automated pipelines for data movement and processing.",
        "is_active": True,
    },
    {
        "id": "big_data_engineer",
        "name": "Big Data Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Develops infrastructure and processing systems for large-scale datasets.",
        "is_active": True,
    },
    {
        "id": "analytics_data_engineer",
        "name": "Analytics Data Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Builds and maintains data infrastructure supporting analytics and business intelligence.",
        "is_active": True,
    },
    {
        "id": "cloud_data_engineer",
        "name": "Cloud Data Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Develops and manages cloud-based data pipelines, storage, and processing systems.",
        "is_active": True,
    },
    {
        "id": "streaming_data_engineer",
        "name": "Streaming Data Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Develops real-time data streaming and event-processing infrastructure.",
        "is_active": True,
    },
    {
        "id": "data_integration_engineer",
        "name": "Data Integration Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Integrates data from multiple sources into consistent and accessible systems.",
        "is_active": True,
    },
    {
        "id": "data_engineering_architect",
        "name": "Data Engineering Architect",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Designs enterprise data engineering architectures, platforms, and integration patterns.",
        "is_active": True,
    },
    {
        "id": "data_platform_engineer",
        "name": "Data Platform Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Builds and operates platforms supporting data ingestion, processing, and consumption.",
        "is_active": True,
    },
    {
        "id": "data_engineering_manager",
        "name": "Data Engineering Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_engineering",
        "description": "Leads data engineering teams, infrastructure delivery, and pipeline development.",
        "is_active": True,
    },
])


# ============================================================
# BIG DATA & DISTRIBUTED SYSTEMS — 8 NEW CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "big_data_developer",
        "name": "Big Data Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Develops applications and processing solutions for large-scale data environments.",
        "is_active": True,
    },
    {
        "id": "hadoop_developer",
        "name": "Hadoop Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Develops distributed data processing solutions using Hadoop technologies.",
        "is_active": True,
    },
    {
        "id": "spark_developer",
        "name": "Spark Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Builds distributed data processing and analytics applications using Apache Spark.",
        "is_active": True,
    },
    {
        "id": "big_data_architect",
        "name": "Big Data Architect",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Designs scalable architectures for distributed storage and large-scale data processing.",
        "is_active": True,
    },
    {
        "id": "data_streaming_engineer",
        "name": "Data Streaming Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Builds distributed real-time data streaming and event-processing systems.",
        "is_active": True,
    },
    {
        "id": "distributed_data_engineer",
        "name": "Distributed Data Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Develops distributed data processing and storage solutions across computing systems.",
        "is_active": True,
    },
    {
        "id": "big_data_platform_engineer",
        "name": "Big Data Platform Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Builds and maintains platforms for distributed data processing and analytics.",
        "is_active": True,
    },
    {
        "id": "big_data_consultant",
        "name": "Big Data Consultant",
        "professional_field_id": "data_analytics",
        "subfield_id": "big_data_distributed_systems",
        "description": "Advises organizations on big data platforms, architectures, and implementation strategies.",
        "is_active": True,
    },
])


# ============================================================
# DATA WAREHOUSING & ARCHITECTURE — 10 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "data_warehouse_engineer",
        "name": "Data Warehouse Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Builds and maintains data warehouse infrastructure and data processing workflows.",
        "is_active": True,
    },
    {
        "id": "data_warehouse_developer",
        "name": "Data Warehouse Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Develops warehouse schemas, data transformations, and analytical data structures.",
        "is_active": True,
    },
    {
        "id": "data_warehouse_architect",
        "name": "Data Warehouse Architect",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Designs enterprise data warehouse architecture, schemas, and integration strategies.",
        "is_active": True,
    },
    {
        "id": "data_warehouse_administrator",
        "name": "Data Warehouse Administrator",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Administers data warehouse platforms, access, availability, and performance.",
        "is_active": True,
    },
    {
        "id": "data_modeling_engineer",
        "name": "Data Modeling Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Designs and implements data models for enterprise storage and analytical systems.",
        "is_active": True,
    },
    {
        "id": "data_modeler",
        "name": "Data Modeler",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Creates conceptual, logical, and physical data models for organizational systems.",
        "is_active": True,
    },
    {
        "id": "cloud_data_warehouse_engineer",
        "name": "Cloud Data Warehouse Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Builds and manages cloud data warehouse environments and analytical workloads.",
        "is_active": True,
    },
    {
        "id": "data_warehouse_consultant",
        "name": "Data Warehouse Consultant",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Advises on data warehouse design, implementation, migration, and optimization.",
        "is_active": True,
    },
    {
        "id": "data_warehouse_etl_developer",
        "name": "Data Warehouse ETL Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Develops ETL workflows that populate and maintain enterprise data warehouses.",
        "is_active": True,
    },
    {
        "id": "data_warehouse_manager",
        "name": "Data Warehouse Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_warehousing_architecture",
        "description": "Oversees data warehouse teams, platforms, operations, and delivery.",
        "is_active": True,
    },
])


# ============================================================
# BUSINESS & PRODUCT ANALYTICS — 9 NEW CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "business_analyst",
        "name": "Business Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Analyzes business needs, processes, and performance to support organizational decisions.",
        "is_active": True,
    },
    {
        "id": "product_analyst",
        "name": "Product Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Analyzes product usage, customer behavior, and product performance metrics.",
        "is_active": True,
    },
    {
        "id": "product_data_analyst",
        "name": "Product Data Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Uses product data to evaluate user engagement, feature performance, and product outcomes.",
        "is_active": True,
    },
    {
        "id": "growth_analyst",
        "name": "Growth Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Analyzes acquisition, retention, conversion, and growth performance.",
        "is_active": True,
    },
    {
        "id": "customer_insights_analyst",
        "name": "Customer Insights Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Analyzes customer behavior, preferences, and feedback to generate business insights.",
        "is_active": True,
    },
    {
        "id": "business_analytics_consultant",
        "name": "Business Analytics Consultant",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Advises organizations on analytical methods, business performance, and data-driven decisions.",
        "is_active": True,
    },
    {
        "id": "product_analytics_manager",
        "name": "Product Analytics Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Leads product analytics strategy, measurement, and insight generation.",
        "is_active": True,
    },
    {
        "id": "business_analytics_manager",
        "name": "Business Analytics Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Manages business analytics teams and organizational performance analysis.",
        "is_active": True,
    },
    {
        "id": "digital_analytics_analyst",
        "name": "Digital Analytics Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "business_product_analytics",
        "description": "Analyzes digital channel, website, and application performance and user behavior.",
        "is_active": True,
    },
])



# ============================================================
# STATISTICAL & QUANTITATIVE ANALYTICS — 8 NEW CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "statistician",
        "name": "Statistician",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Applies statistical methods to collect, analyze, interpret, and communicate data.",
        "is_active": True,
    },
    {
        "id": "quantitative_analyst",
        "name": "Quantitative Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Uses mathematical and statistical models to analyze complex quantitative problems.",
        "is_active": True,
    },
    {
        "id": "quantitative_research_analyst",
        "name": "Quantitative Research Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Conducts quantitative research using statistical analysis and mathematical modeling.",
        "is_active": True,
    },
    {
        "id": "statistical_analyst",
        "name": "Statistical Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Analyzes datasets using statistical techniques to identify patterns and relationships.",
        "is_active": True,
    },
    {
        "id": "econometrician",
        "name": "Econometrician",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Applies statistical and mathematical methods to economic data and relationships.",
        "is_active": True,
    },
    {
        "id": "operations_research_analyst",
        "name": "Operations Research Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Uses mathematical optimization and analytical models to improve operational decisions.",
        "is_active": True,
    },
    {
        "id": "biostatistician",
        "name": "Biostatistician",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Applies statistical methods to biological, medical, and public health research.",
        "is_active": True,
    },
    {
        "id": "quantitative_analytics_manager",
        "name": "Quantitative Analytics Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "statistical_quantitative_analytics",
        "description": "Leads quantitative analytics teams and oversees statistical modeling and analysis.",
        "is_active": True,
    },
])


# ============================================================
# MARKETING, FINANCIAL & OPERATIONS ANALYTICS — 10 ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "marketing_analyst",
        "name": "Marketing Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Analyzes marketing campaigns, channels, and customer data to measure performance.",
        "is_active": True,
    },
    {
        "id": "financial_data_analyst",
        "name": "Financial Data Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Analyzes financial datasets to identify trends and support financial decisions.",
        "is_active": True,
    },
    {
        "id": "financial_analyst",
        "name": "Financial Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Evaluates financial information, performance, and forecasts to support business planning.",
        "is_active": True,
    },
    {
        "id": "operations_analyst",
        "name": "Operations Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Analyzes operational performance, workflows, and business processes.",
        "is_active": True,
    },
    {
        "id": "supply_chain_analyst",
        "name": "Supply Chain Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Analyzes supply chain data, logistics performance, and inventory operations.",
        "is_active": True,
    },
    {
        "id": "revenue_analyst",
        "name": "Revenue Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Analyzes revenue performance, business trends, and revenue opportunities.",
        "is_active": True,
    },
    {
        "id": "pricing_analyst",
        "name": "Pricing Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Evaluates pricing strategies, market data, and profitability through quantitative analysis.",
        "is_active": True,
    },
    {
        "id": "marketing_analytics_manager",
        "name": "Marketing Analytics Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Leads marketing analytics, campaign measurement, and marketing performance reporting.",
        "is_active": True,
    },
    {
        "id": "financial_analytics_manager",
        "name": "Financial Analytics Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Leads financial analytics activities, modeling, and financial performance insights.",
        "is_active": True,
    },
    {
        "id": "operations_analytics_manager",
        "name": "Operations Analytics Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "marketing_financial_operations_analytics",
        "description": "Leads operational analytics and data-driven process improvement initiatives.",
        "is_active": True,
    },
])


# ============================================================
# DATA GOVERNANCE & QUALITY — 10 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "data_governance_analyst",
        "name": "Data Governance Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Supports data governance policies, standards, ownership, and compliance processes.",
        "is_active": True,
    },
    {
        "id": "data_governance_manager",
        "name": "Data Governance Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Leads enterprise data governance frameworks, policies, and accountability.",
        "is_active": True,
    },
    {
        "id": "data_steward",
        "name": "Data Steward",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Maintains data definitions, standards, ownership, and quality across business domains.",
        "is_active": True,
    },
    {
        "id": "data_quality_engineer",
        "name": "Data Quality Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Develops automated checks and processes to validate and improve data quality.",
        "is_active": True,
    },
    {
        "id": "data_quality_manager",
        "name": "Data Quality Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Oversees enterprise data quality standards, monitoring, and improvement programs.",
        "is_active": True,
    },
    {
        "id": "master_data_management_specialist",
        "name": "Master Data Management Specialist",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Manages master data standards, records, consistency, and synchronization across systems.",
        "is_active": True,
    },
    {
        "id": "metadata_management_specialist",
        "name": "Metadata Management Specialist",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Maintains metadata repositories, business glossaries, and data catalog information.",
        "is_active": True,
    },
    {
        "id": "data_compliance_analyst",
        "name": "Data Compliance Analyst",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Monitors data handling practices against privacy, regulatory, and governance requirements.",
        "is_active": True,
    },
    {
        "id": "data_governance_consultant",
        "name": "Data Governance Consultant",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Advises organizations on data governance policies, operating models, and controls.",
        "is_active": True,
    },
    {
        "id": "data_management_lead",
        "name": "Data Management Lead",
        "professional_field_id": "data_analytics",
        "subfield_id": "data_governance_quality",
        "description": "Coordinates data management practices, ownership, standards, and operational processes.",
        "is_active": True,
    },
])


# ============================================================
# ANALYTICS ENGINEERING & DATA MANAGEMENT — 10 ROLES
# ============================================================

CANONICAL_ROLES.extend([
    {
        "id": "analytics_engineer",
        "name": "Analytics Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Transforms, models, and organizes data into reliable datasets for analytics and reporting.",
        "is_active": True,
    },
    {
        "id": "senior_analytics_engineer",
        "name": "Senior Analytics Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Leads analytical data modeling, transformation workflows, and analytics engineering standards.",
        "is_active": True,
    },
    {
        "id": "analytics_architect",
        "name": "Analytics Architect",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Designs analytics architectures, data models, and enterprise analytical environments.",
        "is_active": True,
    },
    {
        "id": "analytics_developer",
        "name": "Analytics Developer",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Develops analytical applications, data transformations, and reporting solutions.",
        "is_active": True,
    },
    {
        "id": "analytics_platform_engineer",
        "name": "Analytics Platform Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Builds and operates platforms supporting analytical workloads and data consumption.",
        "is_active": True,
    },
    {
        "id": "data_management_specialist",
        "name": "Data Management Specialist",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Coordinates data organization, lifecycle management, accessibility, and maintenance.",
        "is_active": True,
    },
    {
        "id": "data_management_consultant",
        "name": "Data Management Consultant",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Advises on enterprise data management strategies, processes, and technology solutions.",
        "is_active": True,
    },
    {
        "id": "analytics_engineering_manager",
        "name": "Analytics Engineering Manager",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Leads analytics engineering teams and manages analytical data development and delivery.",
        "is_active": True,
    },
    {
        "id": "data_solutions_architect",
        "name": "Data Solutions Architect",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Designs integrated data solutions and architectures for organizational requirements.",
        "is_active": True,
    },
    {
        "id": "analytics_solutions_engineer",
        "name": "Analytics Solutions Engineer",
        "professional_field_id": "data_analytics",
        "subfield_id": "analytics_engineering_data_management",
        "description": "Builds and integrates analytics solutions to support business intelligence and decision-making.",
        "is_active": True,
    },
])



# ============================================================
# ENGINEERING & MANUFACTURING
# FIRST FIVE SUBFIELDS
# ============================================================

# 1. MECHANICAL ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "mechanical_engineer",
        "name": "Mechanical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Designs, develops, tests, and improves mechanical systems, machines, and equipment.",
        "is_active": True,
    },
    {
        "id": "design_engineer",
        "name": "Design Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Creates engineering designs, technical drawings, and product specifications.",
        "is_active": True,
    },
    {
        "id": "product_design_engineer",
        "name": "Product Design Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Develops product concepts and mechanical designs for manufacturable products.",
        "is_active": True,
    },
    {
        "id": "cad_design_engineer",
        "name": "CAD Design Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Produces and maintains engineering models and drawings using CAD tools.",
        "is_active": True,
    },
    {
        "id": "hvac_engineer",
        "name": "HVAC Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Designs and oversees heating, ventilation, and air conditioning systems.",
        "is_active": True,
    },
    {
        "id": "thermal_engineer",
        "name": "Thermal Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Analyzes heat transfer, thermal systems, and energy performance of equipment.",
        "is_active": True,
    },
    {
        "id": "automotive_mechanical_engineer",
        "name": "Automotive Mechanical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Develops and improves mechanical systems and components for vehicles.",
        "is_active": True,
    },
    {
        "id": "mechanical_project_engineer",
        "name": "Mechanical Project Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Coordinates mechanical engineering projects, technical execution, and delivery.",
        "is_active": True,
    },
    {
        "id": "maintenance_mechanical_engineer",
        "name": "Maintenance Mechanical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Maintains and improves mechanical equipment, machinery, and industrial systems.",
        "is_active": True,
    },
    {
        "id": "manufacturing_mechanical_engineer",
        "name": "Manufacturing Mechanical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Develops mechanical manufacturing processes and supports production equipment.",
        "is_active": True,
    },
    {
        "id": "mechanical_analysis_engineer",
        "name": "Mechanical Analysis Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Performs mechanical simulations and structural or thermal engineering analysis.",
        "is_active": True,
    },
    {
        "id": "mechanical_engineering_manager",
        "name": "Mechanical Engineering Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "mechanical_engineering",
        "description": "Leads mechanical engineering teams, technical development, and project delivery.",
        "is_active": True,
    },
])


# 2. ELECTRICAL & ELECTRONICS ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "electrical_engineer",
        "name": "Electrical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Designs, develops, and maintains electrical systems and equipment.",
        "is_active": True,
    },
    {
        "id": "electronics_engineer",
        "name": "Electronics Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Designs and tests electronic circuits, components, and systems.",
        "is_active": True,
    },
    {
        "id": "electrical_design_engineer",
        "name": "Electrical Design Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Develops electrical designs, schematics, and technical specifications.",
        "is_active": True,
    },
    {
        "id": "power_systems_engineer",
        "name": "Power Systems Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Designs and analyzes electrical power generation, transmission, and distribution systems.",
        "is_active": True,
    },
    {
        "id": "control_systems_engineer",
        "name": "Control Systems Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Develops control systems for industrial equipment, machines, and processes.",
        "is_active": True,
    },
    {
        "id": "instrumentation_engineer",
        "name": "Instrumentation Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Designs and maintains instrumentation and measurement systems for industrial applications.",
        "is_active": True,
    },
    {
        "id": "electrical_maintenance_engineer",
        "name": "Electrical Maintenance Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Maintains electrical equipment, installations, and industrial power systems.",
        "is_active": True,
    },
    {
        "id": "embedded_electronics_engineer",
        "name": "Embedded Electronics Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Develops electronic hardware and interfaces for embedded applications.",
        "is_active": True,
    },
    {
        "id": "power_electronics_engineer",
        "name": "Power Electronics Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Designs electronic systems for power conversion, regulation, and control.",
        "is_active": True,
    },
    {
        "id": "electrical_project_engineer",
        "name": "Electrical Project Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Manages electrical engineering project planning, execution, and commissioning.",
        "is_active": True,
    },
    {
        "id": "electronics_test_engineer",
        "name": "Electronics Test Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Tests and validates electronic components, circuits, and equipment.",
        "is_active": True,
    },
    {
        "id": "electrical_engineering_manager",
        "name": "Electrical Engineering Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "electrical_electronics_engineering",
        "description": "Leads electrical and electronics engineering teams and technical projects.",
        "is_active": True,
    },
])


# 3. CIVIL & STRUCTURAL ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "civil_engineer",
        "name": "Civil Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Plans, designs, and oversees construction and infrastructure projects.",
        "is_active": True,
    },
    {
        "id": "structural_engineer",
        "name": "Structural Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Designs and assesses structures to ensure strength, stability, and safety.",
        "is_active": True,
    },
    {
        "id": "site_engineer",
        "name": "Site Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Supervises construction site activities, quality, and engineering execution.",
        "is_active": True,
    },
    {
        "id": "construction_engineer",
        "name": "Construction Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Plans and coordinates technical execution of construction projects.",
        "is_active": True,
    },
    {
        "id": "geotechnical_engineer",
        "name": "Geotechnical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Studies soil and rock properties for foundations and infrastructure design.",
        "is_active": True,
    },
    {
        "id": "transportation_engineer",
        "name": "Transportation Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Plans and designs transportation infrastructure and traffic systems.",
        "is_active": True,
    },
    {
        "id": "highway_engineer",
        "name": "Highway Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Designs and oversees highway, road, and pavement engineering projects.",
        "is_active": True,
    },
    {
        "id": "quantity_surveyor",
        "name": "Quantity Surveyor",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Estimates construction costs and manages project quantities and contracts.",
        "is_active": True,
    },
    {
        "id": "bim_engineer",
        "name": "BIM Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Develops and coordinates building information models for construction projects.",
        "is_active": True,
    },
    {
        "id": "civil_project_engineer",
        "name": "Civil Project Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Coordinates civil engineering project planning, design, and execution.",
        "is_active": True,
    },
    {
        "id": "civil_engineering_manager",
        "name": "Civil Engineering Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "civil_structural_engineering",
        "description": "Leads civil engineering teams and oversees infrastructure project delivery.",
        "is_active": True,
    },
])


# 4. CHEMICAL & PROCESS ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "chemical_engineer",
        "name": "Chemical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Designs and improves processes that convert raw materials into useful products.",
        "is_active": True,
    },
    {
        "id": "process_engineer",
        "name": "Process Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Develops and optimizes industrial processes for efficiency, quality, and safety.",
        "is_active": True,
    },
    {
        "id": "process_design_engineer",
        "name": "Process Design Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Designs process systems, equipment specifications, and process flow diagrams.",
        "is_active": True,
    },
    {
        "id": "process_safety_engineer",
        "name": "Process Safety Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Identifies and mitigates hazards in industrial and chemical processes.",
        "is_active": True,
    },
    {
        "id": "chemical_process_engineer",
        "name": "Chemical Process Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Optimizes chemical production processes, process equipment, and plant operations.",
        "is_active": True,
    },
    {
        "id": "production_process_engineer",
        "name": "Production Process Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Improves production processes and supports consistent industrial manufacturing.",
        "is_active": True,
    },
    {
        "id": "petrochemical_engineer",
        "name": "Petrochemical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Develops and supports processes for petroleum and petrochemical production.",
        "is_active": True,
    },
    {
        "id": "process_control_engineer",
        "name": "Process Control Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Develops control strategies and systems for industrial process operations.",
        "is_active": True,
    },
    {
        "id": "chemical_project_engineer",
        "name": "Chemical Project Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Coordinates chemical engineering projects, plant modifications, and process installations.",
        "is_active": True,
    },
    {
        "id": "chemical_engineering_manager",
        "name": "Chemical Engineering Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "chemical_process_engineering",
        "description": "Leads chemical engineering teams and oversees process development and operations.",
        "is_active": True,
    },
])


# 5. INDUSTRIAL & PRODUCTION ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "industrial_engineer",
        "name": "Industrial Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Improves industrial systems, workflows, resource utilization, and productivity.",
        "is_active": True,
    },
    {
        "id": "production_engineer",
        "name": "Production Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Plans and improves production processes, equipment, and manufacturing output.",
        "is_active": True,
    },
    {
        "id": "production_planning_engineer",
        "name": "Production Planning Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Plans production schedules, capacity, and manufacturing resources.",
        "is_active": True,
    },
    {
        "id": "manufacturing_engineer",
        "name": "Manufacturing Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Develops and improves manufacturing methods, processes, and production systems.",
        "is_active": True,
    },
    {
        "id": "lean_manufacturing_engineer",
        "name": "Lean Manufacturing Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Applies lean methods to reduce waste and improve manufacturing efficiency.",
        "is_active": True,
    },
    {
        "id": "continuous_improvement_engineer",
        "name": "Continuous Improvement Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Leads initiatives to improve processes, productivity, and operational performance.",
        "is_active": True,
    },
    {
        "id": "production_planner",
        "name": "Production Planner",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Coordinates production plans, material availability, and manufacturing schedules.",
        "is_active": True,
    },
    {
        "id": "industrial_automation_engineer",
        "name": "Industrial Automation Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Develops automation solutions for manufacturing and industrial operations.",
        "is_active": True,
    },
    {
        "id": "manufacturing_process_engineer",
        "name": "Manufacturing Process Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Optimizes manufacturing processes, production methods, and process capability.",
        "is_active": True,
    },
    {
        "id": "production_supervisor",
        "name": "Production Supervisor",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Supervises production teams, daily output, and manufacturing floor activities.",
        "is_active": True,
    },
    {
        "id": "industrial_engineering_manager",
        "name": "Industrial Engineering Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Leads industrial engineering teams and productivity improvement programs.",
        "is_active": True,
    },
    {
        "id": "production_manager",
        "name": "Production Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "industrial_production_engineering",
        "description": "Manages manufacturing operations, production targets, resources, and teams.",
        "is_active": True,
    },
])



# ============================================================
# ENGINEERING & MANUFACTURING
# NEXT FIVE SUBFIELDS
# ============================================================

# 6. MANUFACTURING & AUTOMATION

CANONICAL_ROLES.extend([
    {
        "id": "automation_engineer",
        "name": "Automation Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "manufacturing_automation",
        "description": "Develops and maintains automated systems and equipment for industrial operations.",
        "is_active": True,
    },
    {
        "id": "plc_programmer",
        "name": "PLC Programmer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "manufacturing_automation",
        "description": "Programs and configures programmable logic controllers for industrial automation.",
        "is_active": True,
    },
    {
        "id": "scada_engineer",
        "name": "SCADA Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "manufacturing_automation",
        "description": "Develops and maintains supervisory control and data acquisition systems.",
        "is_active": True,
    },
    {
        "id": "automation_design_engineer",
        "name": "Automation Design Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "manufacturing_automation",
        "description": "Designs automated machinery, control systems, and industrial automation solutions.",
        "is_active": True,
    },
    {
        "id": "automation_technician",
        "name": "Automation Technician",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "manufacturing_automation",
        "description": "Installs, troubleshoots, and maintains automated industrial equipment.",
        "is_active": True,
    },
    {
        "id": "manufacturing_automation_manager",
        "name": "Manufacturing Automation Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "manufacturing_automation",
        "description": "Leads manufacturing automation projects and industrial technology implementation.",
        "is_active": True,
    },
    {
        "id": "automation_project_engineer",
        "name": "Automation Project Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "manufacturing_automation",
        "description": "Coordinates automation project design, installation, integration, and commissioning.",
        "is_active": True,
    },
])


# 7. AUTOMOTIVE & TRANSPORTATION ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "automotive_engineer",
        "name": "Automotive Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Designs and develops vehicle systems, components, and automotive technologies.",
        "is_active": True,
    },
    {
        "id": "automotive_design_engineer",
        "name": "Automotive Design Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Designs vehicle components, assemblies, and automotive product systems.",
        "is_active": True,
    },
    {
        "id": "automotive_validation_engineer",
        "name": "Automotive Validation Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Validates vehicle systems and components against performance and safety requirements.",
        "is_active": True,
    },
    {
        "id": "vehicle_dynamics_engineer",
        "name": "Vehicle Dynamics Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Analyzes and improves vehicle handling, stability, ride, and dynamic performance.",
        "is_active": True,
    },
    {
        "id": "powertrain_engineer",
        "name": "Powertrain Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Develops and optimizes vehicle propulsion and powertrain systems.",
        "is_active": True,
    },
    {
        "id": "electric_vehicle_engineer",
        "name": "Electric Vehicle Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Develops electric vehicle systems, components, and propulsion technologies.",
        "is_active": True,
    },
    {
        "id": "automotive_systems_engineer",
        "name": "Automotive Systems Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Integrates and develops vehicle-level systems and engineering requirements.",
        "is_active": True,
    },
    {
        "id": "aerospace_engineer",
        "name": "Aerospace Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Designs and develops aircraft, spacecraft, and aerospace systems.",
        "is_active": True,
    },
    {
        "id": "transportation_engineering_specialist",
        "name": "Transportation Engineering Specialist",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Supports the planning and engineering of transportation systems and infrastructure.",
        "is_active": True,
    },
    {
        "id": "automotive_engineering_manager",
        "name": "Automotive Engineering Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "automotive_transportation_engineering",
        "description": "Leads automotive engineering teams and vehicle development programs.",
        "is_active": True,
    },
])


# 8. MATERIALS & METALLURGICAL ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "materials_engineer",
        "name": "Materials Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Develops and evaluates materials for industrial and engineering applications.",
        "is_active": True,
    },
    {
        "id": "metallurgical_engineer",
        "name": "Metallurgical Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Studies and improves metals, alloys, and metallurgical production processes.",
        "is_active": True,
    },
    {
        "id": "materials_scientist",
        "name": "Materials Scientist",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Researches material properties, structures, and applications.",
        "is_active": True,
    },
    {
        "id": "welding_engineer",
        "name": "Welding Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Develops and oversees welding procedures, processes, and quality requirements.",
        "is_active": True,
    },
    {
        "id": "corrosion_engineer",
        "name": "Corrosion Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Prevents and manages material degradation and corrosion in engineering systems.",
        "is_active": True,
    },
    {
        "id": "polymer_engineer",
        "name": "Polymer Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Develops and processes polymer materials and plastic-based products.",
        "is_active": True,
    },
    {
        "id": "composites_engineer",
        "name": "Composites Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Develops and evaluates composite materials and engineered structures.",
        "is_active": True,
    },
    {
        "id": "materials_research_engineer",
        "name": "Materials Research Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Conducts research and testing to develop advanced engineering materials.",
        "is_active": True,
    },
    {
        "id": "metallurgical_process_engineer",
        "name": "Metallurgical Process Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Optimizes metal extraction, refining, and metallurgical processing operations.",
        "is_active": True,
    },
    {
        "id": "materials_engineering_manager",
        "name": "Materials Engineering Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "materials_metallurgical_engineering",
        "description": "Leads materials engineering teams and materials development programs.",
        "is_active": True,
    },
])


# 9. QUALITY, TESTING & RELIABILITY ENGINEERING

CANONICAL_ROLES.extend([
    {
        "id": "quality_engineer",
        "name": "Quality Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Develops and maintains quality processes to ensure products meet requirements.",
        "is_active": True,
    },
    {
        "id": "quality_assurance_engineer",
        "name": "Quality Assurance Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Implements quality assurance procedures and monitors product and process compliance.",
        "is_active": True,
    },
    {
        "id": "quality_control_engineer",
        "name": "Quality Control Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Performs inspections and quality checks to identify product and process defects.",
        "is_active": True,
    },
    {
        "id": "reliability_engineer",
        "name": "Reliability Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Improves equipment and product reliability through testing and failure analysis.",
        "is_active": True,
    },
    {
        "id": "test_engineer",
        "name": "Test Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Develops and performs engineering tests to validate product performance.",
        "is_active": True,
    },
    {
        "id": "validation_engineer",
        "name": "Validation Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Validates engineering products, equipment, and processes against defined specifications.",
        "is_active": True,
    },
    {
        "id": "quality_systems_engineer",
        "name": "Quality Systems Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Maintains quality management systems, standards, audits, and compliance processes.",
        "is_active": True,
    },
    {
        "id": "supplier_quality_engineer",
        "name": "Supplier Quality Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Monitors supplier quality, audits suppliers, and resolves component quality issues.",
        "is_active": True,
    },
    {
        "id": "quality_inspection_engineer",
        "name": "Quality Inspection Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Coordinates technical inspections and verifies product conformity.",
        "is_active": True,
    },
    {
        "id": "quality_manager",
        "name": "Quality Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "quality_testing_reliability_engineering",
        "description": "Leads quality teams, quality systems, audits, and continuous improvement programs.",
        "is_active": True,
    },
])


# 10. ENGINEERING DESIGN & PROJECT EXECUTION

CANONICAL_ROLES.extend([
    {
        "id": "engineering_project_engineer",
        "name": "Engineering Project Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Coordinates engineering project activities, technical deliverables, and execution.",
        "is_active": True,
    },
    {
        "id": "engineering_project_manager",
        "name": "Engineering Project Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Manages engineering project scope, schedules, budgets, resources, and delivery.",
        "is_active": True,
    },
    {
        "id": "engineering_design_manager",
        "name": "Engineering Design Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Leads engineering design teams and oversees design quality and delivery.",
        "is_active": True,
    },
    {
        "id": "project_planning_engineer",
        "name": "Project Planning Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Develops project schedules, tracks milestones, and coordinates planning activities.",
        "is_active": True,
    },
    {
        "id": "project_controls_engineer",
        "name": "Project Controls Engineer",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Monitors project cost, schedule, progress, and performance controls.",
        "is_active": True,
    },
    {
        "id": "engineering_coordinator",
        "name": "Engineering Coordinator",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Coordinates engineering documentation, communication, and project workflows.",
        "is_active": True,
    },
    {
        "id": "technical_project_manager",
        "name": "Technical Project Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Manages technically complex projects and coordinates cross-functional engineering teams.",
        "is_active": True,
    },
    {
        "id": "engineering_consultant",
        "name": "Engineering Consultant",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Provides engineering expertise, technical assessments, and design recommendations.",
        "is_active": True,
    },
    {
        "id": "engineering_design_lead",
        "name": "Engineering Design Lead",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Guides engineering design work and coordinates technical design decisions.",
        "is_active": True,
    },
    {
        "id": "engineering_program_manager",
        "name": "Engineering Program Manager",
        "professional_field_id": "engineering_manufacturing",
        "subfield_id": "engineering_design_project_execution",
        "description": "Oversees multiple related engineering projects and strategic technical programs.",
        "is_active": True,
    },
])



# ============================================================
# FINANCE & ACCOUNTING — FIRST FIVE SUBFIELDS
# ============================================================

# 1. ACCOUNTING & BOOKKEEPING

CANONICAL_ROLES.extend([
    {
        "id": "accountant",
        "name": "Accountant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Maintains financial records, prepares accounts, and supports financial reporting.",
        "is_active": True,
    },
    {
        "id": "senior_accountant",
        "name": "Senior Accountant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Oversees accounting activities, reconciliations, and financial statement preparation.",
        "is_active": True,
    },
    {
        "id": "junior_accountant",
        "name": "Junior Accountant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Supports daily accounting entries, reconciliations, and financial documentation.",
        "is_active": True,
    },
    {
        "id": "accounts_executive",
        "name": "Accounts Executive",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Handles routine accounting operations, invoices, payments, and ledger entries.",
        "is_active": True,
    },
    {
        "id": "accounts_payable_specialist",
        "name": "Accounts Payable Specialist",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Manages supplier invoices, payment processing, and accounts payable records.",
        "is_active": True,
    },
    {
        "id": "accounts_receivable_specialist",
        "name": "Accounts Receivable Specialist",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Manages customer invoices, collections, and accounts receivable records.",
        "is_active": True,
    },
    {
        "id": "bookkeeper",
        "name": "Bookkeeper",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Records and organizes daily financial transactions and bookkeeping entries.",
        "is_active": True,
    },
    {
        "id": "general_ledger_accountant",
        "name": "General Ledger Accountant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Maintains general ledger accounts and performs month-end reconciliations.",
        "is_active": True,
    },
    {
        "id": "cost_accountant",
        "name": "Cost Accountant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Tracks production and operating costs and supports cost control.",
        "is_active": True,
    },
    {
        "id": "accounting_manager",
        "name": "Accounting Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "accounting_bookkeeping",
        "description": "Manages accounting teams, financial records, and reporting processes.",
        "is_active": True,
    },
])


# 2. AUDIT & ASSURANCE

CANONICAL_ROLES.extend([
    {
        "id": "internal_auditor",
        "name": "Internal Auditor",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Evaluates internal controls, operational processes, and organizational risks.",
        "is_active": True,
    },
    {
        "id": "external_auditor",
        "name": "External Auditor",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Independently examines financial statements and verifies reporting accuracy.",
        "is_active": True,
    },
    {
        "id": "audit_associate",
        "name": "Audit Associate",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Supports audit engagements through testing, documentation, and financial verification.",
        "is_active": True,
    },
    {
        "id": "audit_senior",
        "name": "Audit Senior",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Supervises audit assignments and reviews financial and control evidence.",
        "is_active": True,
    },
    {
        "id": "audit_manager",
        "name": "Audit Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Manages audit engagements, teams, timelines, and client deliverables.",
        "is_active": True,
    },
    {
        "id": "forensic_accountant",
        "name": "Forensic Accountant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Investigates financial irregularities, fraud, and disputed transactions.",
        "is_active": True,
    },
    {
        "id": "it_auditor",
        "name": "IT Auditor",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Assesses information systems, technology controls, and IT-related risks.",
        "is_active": True,
    },
    {
        "id": "compliance_auditor",
        "name": "Compliance Auditor",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Reviews organizational compliance with applicable regulations and standards.",
        "is_active": True,
    },
    {
        "id": "audit_analyst",
        "name": "Audit Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Analyzes audit data, identifies control gaps, and prepares audit reports.",
        "is_active": True,
    },
    {
        "id": "head_of_internal_audit",
        "name": "Head of Internal Audit",
        "professional_field_id": "finance_accounting",
        "subfield_id": "audit_assurance",
        "description": "Leads internal audit strategy, governance reviews, and assurance functions.",
        "is_active": True,
    },
])


# 3. TAXATION

CANONICAL_ROLES.extend([
    {
        "id": "tax_accountant",
        "name": "Tax Accountant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Prepares tax calculations, returns, and supporting financial documentation.",
        "is_active": True,
    },
    {
        "id": "tax_analyst",
        "name": "Tax Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Analyzes tax regulations, liabilities, and tax reporting requirements.",
        "is_active": True,
    },
    {
        "id": "tax_consultant",
        "name": "Tax Consultant",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Advises individuals and organizations on tax planning and compliance.",
        "is_active": True,
    },
    {
        "id": "tax_manager",
        "name": "Tax Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Oversees tax compliance, planning, reporting, and tax team operations.",
        "is_active": True,
    },
    {
        "id": "corporate_tax_specialist",
        "name": "Corporate Tax Specialist",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Handles corporate tax calculations, filings, and regulatory requirements.",
        "is_active": True,
    },
    {
        "id": "international_tax_specialist",
        "name": "International Tax Specialist",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Supports cross-border tax planning, international taxation, and compliance.",
        "is_active": True,
    },
    {
        "id": "gst_specialist",
        "name": "GST Specialist",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Manages goods and services tax compliance, returns, and reconciliations.",
        "is_active": True,
    },
    {
        "id": "transfer_pricing_analyst",
        "name": "Transfer Pricing Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Analyzes related-party transactions and prepares transfer pricing documentation.",
        "is_active": True,
    },
    {
        "id": "tax_compliance_specialist",
        "name": "Tax Compliance Specialist",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Ensures timely and accurate tax filings and compliance documentation.",
        "is_active": True,
    },
    {
        "id": "tax_director",
        "name": "Tax Director",
        "professional_field_id": "finance_accounting",
        "subfield_id": "taxation",
        "description": "Leads organizational tax strategy, governance, and tax risk management.",
        "is_active": True,
    },
])


# 4. FINANCIAL MANAGEMENT & CONTROLLING

CANONICAL_ROLES.extend([
    {
        "id": "finance_manager",
        "name": "Finance Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Manages financial operations, reporting, budgets, and financial controls.",
        "is_active": True,
    },
    {
        "id": "financial_controller",
        "name": "Financial Controller",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Oversees financial reporting, accounting controls, and financial governance.",
        "is_active": True,
    },
    {
        "id": "finance_controller",
        "name": "Finance Controller",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Manages finance control activities, reporting accuracy, and financial processes.",
        "is_active": True,
    },
    {
        "id": "financial_control_analyst",
        "name": "Financial Control Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Monitors financial controls, reconciliations, and reporting processes.",
        "is_active": True,
    },
    {
        "id": "finance_business_partner",
        "name": "Finance Business Partner",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Partners with business teams to support financial decisions and performance.",
        "is_active": True,
    },
    {
        "id": "treasury_analyst",
        "name": "Treasury Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Analyzes cash positions, liquidity, funding, and treasury activities.",
        "is_active": True,
    },
    {
        "id": "treasury_manager",
        "name": "Treasury Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Manages organizational liquidity, cash management, and financial risk.",
        "is_active": True,
    },
    {
        "id": "financial_reporting_manager",
        "name": "Financial Reporting Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Leads financial statement preparation, reporting cycles, and disclosures.",
        "is_active": True,
    },
    {
        "id": "financial_operations_manager",
        "name": "Financial Operations Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Oversees financial operations, transaction processes, and operational controls.",
        "is_active": True,
    },
    {
        "id": "chief_financial_officer",
        "name": "Chief Financial Officer",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_management_controlling",
        "description": "Leads enterprise financial strategy, governance, and financial performance.",
        "is_active": True,
    },
])


# 5. FINANCIAL PLANNING & ANALYSIS

CANONICAL_ROLES.extend([
    {
        "id": "financial_planning_analyst",
        "name": "Financial Planning Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Supports financial planning, budgeting, forecasting, and performance analysis.",
        "is_active": True,
    },
    {
        "id": "fp_and_a_analyst",
        "name": "FP&A Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Analyzes financial performance and prepares budgets, forecasts, and management reports.",
        "is_active": True,
    },
    {
        "id": "senior_fp_and_a_analyst",
        "name": "Senior FP&A Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Leads complex financial analysis, forecasting, and planning activities.",
        "is_active": True,
    },
    {
        "id": "financial_planning_manager",
        "name": "Financial Planning Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Manages financial planning processes, budgets, and long-term forecasts.",
        "is_active": True,
    },
    {
        "id": "fp_and_a_manager",
        "name": "FP&A Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Leads financial planning and analysis teams and business performance reviews.",
        "is_active": True,
    },
    {
        "id": "budget_analyst",
        "name": "Budget Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Develops and monitors budgets and analyzes spending against financial plans.",
        "is_active": True,
    },
    {
        "id": "forecasting_analyst",
        "name": "Forecasting Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Develops financial forecasts using historical performance and business assumptions.",
        "is_active": True,
    },
    {
        "id": "financial_modeling_analyst",
        "name": "Financial Modeling Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Builds financial models to evaluate business performance and future scenarios.",
        "is_active": True,
    },
    {
        "id": "corporate_finance_analyst",
        "name": "Corporate Finance Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Supports corporate financial decisions through financial analysis and modeling.",
        "is_active": True,
    },
    {
        "id": "director_of_fp_and_a",
        "name": "Director of FP&A",
        "professional_field_id": "finance_accounting",
        "subfield_id": "financial_planning_analysis",
        "description": "Directs enterprise financial planning, forecasting, and performance management.",
        "is_active": True,
    },
])



# ============================================================
# FINANCE & ACCOUNTING — FINAL THREE SUBFIELDS
# ============================================================

# 6. BANKING & CREDIT

CANONICAL_ROLES.extend([
    {
        "id": "banking_associate",
        "name": "Banking Associate",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Supports banking operations, customer transactions, and financial services.",
        "is_active": True,
    },
    {
        "id": "relationship_manager_banking",
        "name": "Banking Relationship Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Manages banking client relationships and recommends financial products and services.",
        "is_active": True,
    },
    {
        "id": "credit_analyst",
        "name": "Credit Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Evaluates borrower creditworthiness, financial statements, and repayment risks.",
        "is_active": True,
    },
    {
        "id": "credit_manager",
        "name": "Credit Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Oversees credit assessments, lending decisions, and credit risk controls.",
        "is_active": True,
    },
    {
        "id": "loan_officer",
        "name": "Loan Officer",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Processes loan applications and evaluates borrower eligibility.",
        "is_active": True,
    },
    {
        "id": "banking_operations_analyst",
        "name": "Banking Operations Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Analyzes and improves banking transaction and operational processes.",
        "is_active": True,
    },
    {
        "id": "branch_manager_banking",
        "name": "Bank Branch Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Manages branch operations, staff, customer relationships, and business targets.",
        "is_active": True,
    },
    {
        "id": "credit_risk_analyst",
        "name": "Credit Risk Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Measures and monitors risks associated with lending and credit portfolios.",
        "is_active": True,
    },
    {
        "id": "trade_finance_specialist",
        "name": "Trade Finance Specialist",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Handles trade finance products, international transactions, and related documentation.",
        "is_active": True,
    },
    {
        "id": "banking_manager",
        "name": "Banking Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "banking_credit",
        "description": "Leads banking teams and oversees financial services and banking operations.",
        "is_active": True,
    },
])


# 7. INVESTMENT & ASSET MANAGEMENT

CANONICAL_ROLES.extend([
    {
        "id": "investment_analyst",
        "name": "Investment Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Researches investment opportunities and evaluates financial assets and markets.",
        "is_active": True,
    },
    {
        "id": "equity_research_analyst",
        "name": "Equity Research Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Analyzes companies, securities, and equity markets to produce investment research.",
        "is_active": True,
    },
    {
        "id": "portfolio_manager",
        "name": "Portfolio Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Manages investment portfolios according to financial objectives and risk parameters.",
        "is_active": True,
    },
    {
        "id": "asset_manager",
        "name": "Asset Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Manages financial assets and investment strategies for clients or institutions.",
        "is_active": True,
    },
    {
        "id": "investment_banker",
        "name": "Investment Banker",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Advises organizations on capital raising, mergers, acquisitions, and financial transactions.",
        "is_active": True,
    },
    {
        "id": "fund_manager",
        "name": "Fund Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Oversees investment funds, asset allocation, and portfolio performance.",
        "is_active": True,
    },
    {
        "id": "wealth_manager",
        "name": "Wealth Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Provides investment and financial planning services to individual and institutional clients.",
        "is_active": True,
    },
    {
        "id": "investment_operations_analyst",
        "name": "Investment Operations Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Supports investment operations, trade processing, settlements, and portfolio reporting.",
        "is_active": True,
    },
    {
        "id": "private_equity_analyst",
        "name": "Private Equity Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Evaluates private company investments, financial performance, and transaction opportunities.",
        "is_active": True,
    },
    {
        "id": "investment_management_director",
        "name": "Investment Management Director",
        "professional_field_id": "finance_accounting",
        "subfield_id": "investment_asset_management",
        "description": "Leads investment management strategy, portfolio teams, and asset allocation decisions.",
        "is_active": True,
    },
])


# 8. INSURANCE & RISK MANAGEMENT

CANONICAL_ROLES.extend([
    {
        "id": "insurance_analyst",
        "name": "Insurance Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Analyzes insurance data, policies, claims, and business performance.",
        "is_active": True,
    },
    {
        "id": "insurance_underwriter",
        "name": "Insurance Underwriter",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Evaluates insurance applications and determines coverage and premium terms.",
        "is_active": True,
    },
    {
        "id": "insurance_claims_analyst",
        "name": "Insurance Claims Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Reviews insurance claims and assesses documentation, coverage, and settlement requirements.",
        "is_active": True,
    },
    {
        "id": "claims_adjuster",
        "name": "Claims Adjuster",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Investigates insurance claims and evaluates the extent of covered losses.",
        "is_active": True,
    },
    {
        "id": "actuary",
        "name": "Actuary",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Uses mathematics and statistics to evaluate financial and insurance risks.",
        "is_active": True,
    },
    {
        "id": "risk_analyst",
        "name": "Risk Analyst",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Identifies, measures, and monitors financial and operational risks.",
        "is_active": True,
    },
    {
        "id": "risk_manager",
        "name": "Risk Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Leads organizational risk assessment, mitigation, and monitoring activities.",
        "is_active": True,
    },
    {
        "id": "insurance_manager",
        "name": "Insurance Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Manages insurance operations, underwriting, claims, and business relationships.",
        "is_active": True,
    },
    {
        "id": "enterprise_risk_manager",
        "name": "Enterprise Risk Manager",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Oversees enterprise-wide risk frameworks, governance, and mitigation strategies.",
        "is_active": True,
    },
    {
        "id": "insurance_broker",
        "name": "Insurance Broker",
        "professional_field_id": "finance_accounting",
        "subfield_id": "insurance_risk_management",
        "description": "Advises clients and arranges suitable insurance coverage with providers.",
        "is_active": True,
    },
])



# ============================================================
# SALES & BUSINESS DEVELOPMENT — FIRST FIVE SUBFIELDS
# ============================================================

# 1. BUSINESS DEVELOPMENT & PARTNERSHIPS

CANONICAL_ROLES.extend([
    {
        "id": "business_development_executive",
        "name": "Business Development Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Identifies new business opportunities, develops prospects, and generates revenue.",
        "is_active": True,
    },
    {
        "id": "business_development_manager",
        "name": "Business Development Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Leads business growth initiatives, strategic prospecting, and opportunity development.",
        "is_active": True,
    },
    {
        "id": "business_development_associate",
        "name": "Business Development Associate",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Supports market research, lead generation, and business development activities.",
        "is_active": True,
    },
    {
        "id": "partnerships_manager",
        "name": "Partnerships Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Develops and manages strategic partnerships and commercial relationships.",
        "is_active": True,
    },
    {
        "id": "strategic_partnerships_manager",
        "name": "Strategic Partnerships Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Builds strategic alliances that support long-term business growth.",
        "is_active": True,
    },
    {
        "id": "business_development_director",
        "name": "Business Development Director",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Directs business development strategy, market expansion, and growth opportunities.",
        "is_active": True,
    },
    {
        "id": "channel_partnerships_manager",
        "name": "Channel Partnerships Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Develops and manages reseller, distributor, and channel partner relationships.",
        "is_active": True,
    },
    {
        "id": "corporate_development_manager",
        "name": "Corporate Development Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Evaluates strategic growth initiatives, acquisitions, and corporate opportunities.",
        "is_active": True,
    },
    {
        "id": "business_growth_manager",
        "name": "Business Growth Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "business_development_partnerships",
        "description": "Drives business expansion through new markets, customers, and revenue opportunities.",
        "is_active": True,
    },
])


# 2. INSIDE & FIELD SALES

CANONICAL_ROLES.extend([
    {
        "id": "sales_executive",
        "name": "Sales Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Promotes products and services, manages prospects, and achieves sales targets.",
        "is_active": True,
    },
    {
        "id": "inside_sales_executive",
        "name": "Inside Sales Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Generates and converts sales opportunities through phone, email, and online channels.",
        "is_active": True,
    },
    {
        "id": "inside_sales_representative",
        "name": "Inside Sales Representative",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Contacts prospective customers remotely and manages the sales process.",
        "is_active": True,
    },
    {
        "id": "field_sales_executive",
        "name": "Field Sales Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Develops customer relationships and generates sales through in-person visits.",
        "is_active": True,
    },
    {
        "id": "field_sales_manager",
        "name": "Field Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Leads field sales teams, territory coverage, and sales performance.",
        "is_active": True,
    },
    {
        "id": "sales_representative",
        "name": "Sales Representative",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Represents an organization in customer acquisition and product or service sales.",
        "is_active": True,
    },
    {
        "id": "territory_sales_manager",
        "name": "Territory Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Manages sales activities, customers, and revenue targets within an assigned territory.",
        "is_active": True,
    },
    {
        "id": "regional_sales_manager",
        "name": "Regional Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Oversees sales teams and business performance across a geographic region.",
        "is_active": True,
    },
    {
        "id": "sales_manager",
        "name": "Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Manages sales personnel, customer acquisition, and revenue targets.",
        "is_active": True,
    },
    {
        "id": "sales_director",
        "name": "Sales Director",
        "professional_field_id": "sales_business_development",
        "subfield_id": "inside_field_sales",
        "description": "Leads sales strategy, revenue growth, and sales organization performance.",
        "is_active": True,
    },
])


# 3. ENTERPRISE & B2B SALES

CANONICAL_ROLES.extend([
    {
        "id": "b2b_sales_executive",
        "name": "B2B Sales Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Sells products and services to business customers and corporate accounts.",
        "is_active": True,
    },
    {
        "id": "enterprise_sales_executive",
        "name": "Enterprise Sales Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Develops and closes complex sales opportunities with large organizations.",
        "is_active": True,
    },
    {
        "id": "enterprise_sales_manager",
        "name": "Enterprise Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Leads enterprise sales teams and manages strategic corporate opportunities.",
        "is_active": True,
    },
    {
        "id": "key_account_sales_manager",
        "name": "Key Account Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Manages high-value enterprise customers and strategic sales relationships.",
        "is_active": True,
    },
    {
        "id": "strategic_account_executive",
        "name": "Strategic Account Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Develops and closes strategic sales opportunities with major accounts.",
        "is_active": True,
    },
    {
        "id": "corporate_sales_manager",
        "name": "Corporate Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Manages corporate sales activities and business customer relationships.",
        "is_active": True,
    },
    {
        "id": "national_sales_manager",
        "name": "National Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Leads nationwide sales strategy, teams, and enterprise revenue performance.",
        "is_active": True,
    },
    {
        "id": "global_account_manager",
        "name": "Global Account Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Manages multinational customer relationships and global enterprise accounts.",
        "is_active": True,
    },
    {
        "id": "b2b_sales_director",
        "name": "B2B Sales Director",
        "professional_field_id": "sales_business_development",
        "subfield_id": "enterprise_b2b_sales",
        "description": "Directs business-to-business sales strategy and enterprise revenue growth.",
        "is_active": True,
    },
])


# 4. ACCOUNT MANAGEMENT & CLIENT RELATIONS

CANONICAL_ROLES.extend([
    {
        "id": "account_manager",
        "name": "Account Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Manages customer accounts, relationships, retention, and account growth.",
        "is_active": True,
    },
    {
        "id": "key_account_manager",
        "name": "Key Account Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Manages important customer accounts and develops long-term commercial relationships.",
        "is_active": True,
    },
    {
        "id": "client_relationship_manager",
        "name": "Client Relationship Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Maintains client relationships and coordinates ongoing service and business needs.",
        "is_active": True,
    },
    {
        "id": "client_account_executive",
        "name": "Client Account Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Coordinates client accounts, commercial requirements, and account development.",
        "is_active": True,
    },
    {
        "id": "strategic_account_manager",
        "name": "Strategic Account Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Develops strategic customer accounts and manages long-term account value.",
        "is_active": True,
    },
    {
        "id": "account_director",
        "name": "Account Director",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Oversees major client accounts, account teams, and commercial relationships.",
        "is_active": True,
    },
    {
        "id": "client_services_manager",
        "name": "Client Services Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Manages client service delivery, satisfaction, and relationship operations.",
        "is_active": True,
    },
    {
        "id": "account_management_director",
        "name": "Account Management Director",
        "professional_field_id": "sales_business_development",
        "subfield_id": "account_management_client_relations",
        "description": "Leads account management strategy, teams, retention, and customer growth.",
        "is_active": True,
    },
])


# 5. SALES OPERATIONS & ENABLEMENT

CANONICAL_ROLES.extend([
    {
        "id": "sales_operations_analyst",
        "name": "Sales Operations Analyst",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Analyzes sales performance, pipeline data, processes, and operational metrics.",
        "is_active": True,
    },
    {
        "id": "sales_operations_manager",
        "name": "Sales Operations Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Manages sales processes, systems, reporting, and operational effectiveness.",
        "is_active": True,
    },
    {
        "id": "sales_enablement_manager",
        "name": "Sales Enablement Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Develops training, resources, and tools to improve sales team effectiveness.",
        "is_active": True,
    },
    {
        "id": "sales_enablement_specialist",
        "name": "Sales Enablement Specialist",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Creates sales resources, training materials, and onboarding support.",
        "is_active": True,
    },
    {
        "id": "sales_analyst",
        "name": "Sales Analyst",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Analyzes sales trends, revenue performance, and customer acquisition metrics.",
        "is_active": True,
    },
    {
        "id": "salesforce_administrator",
        "name": "Salesforce Administrator",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Configures and maintains Salesforce CRM systems supporting sales operations.",
        "is_active": True,
    },
    {
        "id": "sales_compensation_analyst",
        "name": "Sales Compensation Analyst",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Analyzes sales incentives, commissions, and compensation plans.",
        "is_active": True,
    },
    {
        "id": "sales_strategy_manager",
        "name": "Sales Strategy Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Develops sales strategies, performance frameworks, and revenue growth plans.",
        "is_active": True,
    },
    {
        "id": "revenue_operations_manager",
        "name": "Revenue Operations Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "sales_operations_enablement",
        "description": "Coordinates revenue operations across sales processes, systems, and reporting.",
        "is_active": True,
    },
])


# ============================================================
# SALES & BUSINESS DEVELOPMENT — FINAL TWO SUBFIELDS
# ============================================================

# 6. CHANNEL & RETAIL SALES

CANONICAL_ROLES.extend([
    {
        "id": "channel_sales_executive",
        "name": "Channel Sales Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Develops sales through distributors, resellers, and channel partners.",
        "is_active": True,
    },
    {
        "id": "channel_sales_manager",
        "name": "Channel Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Manages channel sales strategy, partner networks, and indirect revenue.",
        "is_active": True,
    },
    {
        "id": "retail_sales_executive",
        "name": "Retail Sales Executive",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Assists retail customers and drives product sales in retail environments.",
        "is_active": True,
    },
    {
        "id": "retail_sales_manager",
        "name": "Retail Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Manages retail sales teams, store revenue, and customer acquisition.",
        "is_active": True,
    },
    {
        "id": "distributor_sales_manager",
        "name": "Distributor Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Manages distributor relationships, sales targets, and distribution performance.",
        "is_active": True,
    },
    {
        "id": "channel_account_manager",
        "name": "Channel Account Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Manages commercial relationships and performance of channel accounts.",
        "is_active": True,
    },
    {
        "id": "channel_development_manager",
        "name": "Channel Development Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Expands channel networks and develops new distribution partnerships.",
        "is_active": True,
    },
    {
        "id": "retail_store_sales_supervisor",
        "name": "Retail Store Sales Supervisor",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Supervises retail sales staff and daily store sales activities.",
        "is_active": True,
    },
    {
        "id": "regional_channel_manager",
        "name": "Regional Channel Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "channel_retail_sales",
        "description": "Oversees channel partners and indirect sales across a geographic region.",
        "is_active": True,
    },
])


# 7. PRE-SALES & SOLUTIONS CONSULTING

CANONICAL_ROLES.extend([
    {
        "id": "presales_consultant",
        "name": "Pre-Sales Consultant",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Supports sales teams through product demonstrations and technical presentations.",
        "is_active": True,
    },
    {
        "id": "solutions_consultant",
        "name": "Solutions Consultant",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Recommends solutions aligned with customer business and technical requirements.",
        "is_active": True,
    },
    {
        "id": "solutions_engineer",
        "name": "Solutions Engineer",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Designs and demonstrates technical solutions to support customer sales opportunities.",
        "is_active": True,
    },
    {
        "id": "sales_engineer",
        "name": "Sales Engineer",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Combines technical expertise and sales support to explain product capabilities.",
        "is_active": True,
    },
    {
        "id": "technical_presales_engineer",
        "name": "Technical Pre-Sales Engineer",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Provides technical evaluations, product demonstrations, and solution guidance before purchase.",
        "is_active": True,
    },
    {
        "id": "presales_manager",
        "name": "Pre-Sales Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Leads pre-sales teams and manages technical sales support activities.",
        "is_active": True,
    },
    {
        "id": "solutions_architect_presales",
        "name": "Pre-Sales Solutions Architect",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Designs solution architectures and technical proposals for prospective customers.",
        "is_active": True,
    },
    {
        "id": "sales_consulting_manager",
        "name": "Sales Consulting Manager",
        "professional_field_id": "sales_business_development",
        "subfield_id": "presales_solutions_consulting",
        "description": "Leads consulting support for customer acquisition and solution-based sales.",
        "is_active": True,
    },
])


# ============================================================
# MARKETING & COMMUNICATIONS — FIRST THREE SUBFIELDS
# ============================================================

# 1. DIGITAL & PERFORMANCE MARKETING

CANONICAL_ROLES.extend([
    {
        "id": "digital_marketing_executive",
        "name": "Digital Marketing Executive",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Executes digital marketing campaigns across online channels.",
        "is_active": True,
    },
    {
        "id": "digital_marketing_manager",
        "name": "Digital Marketing Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Manages digital marketing strategy, channels, budgets, and campaign performance.",
        "is_active": True,
    },
    {
        "id": "performance_marketing_manager",
        "name": "Performance Marketing Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Leads measurable advertising campaigns focused on acquisition and conversions.",
        "is_active": True,
    },
    {
        "id": "performance_marketing_specialist",
        "name": "Performance Marketing Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Optimizes paid marketing campaigns to improve acquisition and return on investment.",
        "is_active": True,
    },
    {
        "id": "seo_specialist",
        "name": "SEO Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Improves organic search visibility through technical and content optimization.",
        "is_active": True,
    },
    {
        "id": "seo_manager",
        "name": "SEO Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Leads search engine optimization strategy and organic growth initiatives.",
        "is_active": True,
    },
    {
        "id": "sem_specialist",
        "name": "SEM Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Manages paid search campaigns and search advertising performance.",
        "is_active": True,
    },
    {
        "id": "paid_media_specialist",
        "name": "Paid Media Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Plans and optimizes paid advertising across digital media platforms.",
        "is_active": True,
    },
    {
        "id": "social_media_marketing_manager",
        "name": "Social Media Marketing Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Manages social media campaigns, audience growth, and channel performance.",
        "is_active": True,
    },
    {
        "id": "digital_campaign_manager",
        "name": "Digital Campaign Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "digital_performance_marketing",
        "description": "Plans and coordinates digital campaigns across marketing channels.",
        "is_active": True,
    },
])


# 2. BRAND & PRODUCT MARKETING

CANONICAL_ROLES.extend([
    {
        "id": "brand_manager",
        "name": "Brand Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Manages brand positioning, identity, campaigns, and market presence.",
        "is_active": True,
    },
    {
        "id": "assistant_brand_manager",
        "name": "Assistant Brand Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Supports brand strategy, campaign execution, and brand performance analysis.",
        "is_active": True,
    },
    {
        "id": "brand_marketing_manager",
        "name": "Brand Marketing Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Leads marketing initiatives that strengthen brand awareness and positioning.",
        "is_active": True,
    },
    {
        "id": "product_marketing_manager",
        "name": "Product Marketing Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Develops product positioning, messaging, launches, and go-to-market strategies.",
        "is_active": True,
    },
    {
        "id": "product_marketing_specialist",
        "name": "Product Marketing Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Supports product messaging, market research, and marketing campaign execution.",
        "is_active": True,
    },
    {
        "id": "go_to_market_manager",
        "name": "Go-to-Market Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Coordinates go-to-market plans for products, services, and new offerings.",
        "is_active": True,
    },
    {
        "id": "brand_strategy_manager",
        "name": "Brand Strategy Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Defines brand strategy, positioning, and long-term brand development.",
        "is_active": True,
    },
    {
        "id": "product_launch_manager",
        "name": "Product Launch Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Plans and coordinates product launch marketing activities.",
        "is_active": True,
    },
    {
        "id": "brand_director",
        "name": "Brand Director",
        "professional_field_id": "marketing_communications",
        "subfield_id": "brand_product_marketing",
        "description": "Directs brand strategy, marketing investment, and brand portfolio performance.",
        "is_active": True,
    },
])


# 3. CONTENT, COPYWRITING & COMMUNICATIONS

CANONICAL_ROLES.extend([
    {
        "id": "content_writer",
        "name": "Content Writer",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Creates written content for websites, campaigns, and digital platforms.",
        "is_active": True,
    },
    {
        "id": "content_marketing_manager",
        "name": "Content Marketing Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Leads content strategy and distribution to attract and engage target audiences.",
        "is_active": True,
    },
    {
        "id": "content_strategist",
        "name": "Content Strategist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Develops content plans aligned with audience needs and business objectives.",
        "is_active": True,
    },
    {
        "id": "copywriter",
        "name": "Copywriter",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Writes persuasive marketing and advertising copy for customer engagement.",
        "is_active": True,
    },
    {
        "id": "senior_copywriter",
        "name": "Senior Copywriter",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Creates and reviews high-impact copy across marketing and communication channels.",
        "is_active": True,
    },
    {
        "id": "technical_content_writer",
        "name": "Technical Content Writer",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Creates technical articles, documentation, and educational content.",
        "is_active": True,
    },
    {
        "id": "content_editor",
        "name": "Content Editor",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Edits and reviews written content for clarity, accuracy, and consistency.",
        "is_active": True,
    },
    {
        "id": "content_manager",
        "name": "Content Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Manages content production, editorial workflows, and publishing schedules.",
        "is_active": True,
    },
    {
        "id": "communications_specialist",
        "name": "Communications Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Develops organizational and external communications materials.",
        "is_active": True,
    },
    {
        "id": "content_director",
        "name": "Content Director",
        "professional_field_id": "marketing_communications",
        "subfield_id": "content_copywriting_communications",
        "description": "Directs content strategy, editorial teams, and publishing operations.",
        "is_active": True,
    },
])



# ============================================================
# MARKETING & COMMUNICATIONS — FINAL THREE SUBFIELDS
# ============================================================

# 4. PUBLIC RELATIONS & CORPORATE COMMUNICATIONS

CANONICAL_ROLES.extend([
    {
        "id": "public_relations_specialist",
        "name": "Public Relations Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Manages media relations, publicity, and external communications.",
        "is_active": True,
    },
    {
        "id": "public_relations_manager",
        "name": "Public Relations Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Leads public relations strategy, media engagement, and reputation management.",
        "is_active": True,
    },
    {
        "id": "corporate_communications_manager",
        "name": "Corporate Communications Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Manages internal and external corporate communication programs.",
        "is_active": True,
    },
    {
        "id": "communications_manager",
        "name": "Communications Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Coordinates organizational messaging and communication activities.",
        "is_active": True,
    },
    {
        "id": "media_relations_manager",
        "name": "Media Relations Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Builds relationships with journalists and manages media engagement.",
        "is_active": True,
    },
    {
        "id": "publicity_manager",
        "name": "Publicity Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Plans publicity campaigns and manages public visibility initiatives.",
        "is_active": True,
    },
    {
        "id": "internal_communications_manager",
        "name": "Internal Communications Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Manages employee communications and internal messaging programs.",
        "is_active": True,
    },
    {
        "id": "corporate_affairs_manager",
        "name": "Corporate Affairs Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Coordinates corporate reputation, stakeholder engagement, and public affairs.",
        "is_active": True,
    },
    {
        "id": "public_relations_director",
        "name": "Public Relations Director",
        "professional_field_id": "marketing_communications",
        "subfield_id": "public_relations_corporate_communications",
        "description": "Directs public relations strategy and organizational reputation initiatives.",
        "is_active": True,
    },
])


# 5. MARKET RESEARCH & CONSUMER INSIGHTS

CANONICAL_ROLES.extend([
    {
        "id": "market_research_analyst",
        "name": "Market Research Analyst",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Studies markets, competitors, and customer behavior to support business decisions.",
        "is_active": True,
    },
    {
        "id": "market_research_manager",
        "name": "Market Research Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Leads market research programs and translates findings into business insights.",
        "is_active": True,
    },
    {
        "id": "consumer_insights_analyst",
        "name": "Consumer Insights Analyst",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Analyzes consumer behavior, preferences, and purchasing patterns.",
        "is_active": True,
    },
    {
        "id": "consumer_insights_manager",
        "name": "Consumer Insights Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Leads consumer research and develops actionable customer insights.",
        "is_active": True,
    },
    {
        "id": "market_intelligence_analyst",
        "name": "Market Intelligence Analyst",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Monitors market trends, competitor activity, and industry developments.",
        "is_active": True,
    },
    {
        "id": "competitive_intelligence_analyst",
        "name": "Competitive Intelligence Analyst",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Researches competitors and evaluates competitive market positioning.",
        "is_active": True,
    },
    {
        "id": "customer_research_analyst",
        "name": "Customer Research Analyst",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Conducts research into customer needs, satisfaction, and experiences.",
        "is_active": True,
    },
    {
        "id": "market_research_director",
        "name": "Market Research Director",
        "professional_field_id": "marketing_communications",
        "subfield_id": "market_research_consumer_insights",
        "description": "Directs market research strategy, teams, and insights programs.",
        "is_active": True,
    },
])


# 6. MARKETING STRATEGY & OPERATIONS

CANONICAL_ROLES.extend([
    {
        "id": "marketing_manager",
        "name": "Marketing Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "marketing_strategy_operations",
        "description": "Plans and manages marketing activities, budgets, and campaigns.",
        "is_active": True,
    },
    {
        "id": "marketing_director",
        "name": "Marketing Director",
        "professional_field_id": "marketing_communications",
        "subfield_id": "marketing_strategy_operations",
        "description": "Directs marketing strategy, teams, budgets, and organizational growth initiatives.",
        "is_active": True,
    },
    {
        "id": "marketing_strategy_manager",
        "name": "Marketing Strategy Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "marketing_strategy_operations",
        "description": "Develops marketing strategies aligned with business and customer objectives.",
        "is_active": True,
    },
    {
        "id": "marketing_operations_manager",
        "name": "Marketing Operations Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "marketing_strategy_operations",
        "description": "Manages marketing processes, technology, reporting, and operational efficiency.",
        "is_active": True,
    },
    {
        "id": "marketing_operations_specialist",
        "name": "Marketing Operations Specialist",
        "professional_field_id": "marketing_communications",
        "subfield_id": "marketing_strategy_operations",
        "description": "Supports marketing systems, workflows, campaign operations, and reporting.",
        "is_active": True,
    },
    {
        "id": "marketing_automation_manager",
        "name": "Marketing Automation Manager",
        "professional_field_id": "marketing_communications",
        "subfield_id": "marketing_strategy_operations",
        "description": "Manages marketing automation platforms, workflows, and campaign processes.",
        "is_active": True,
    },
    {
        "id": "chief_marketing_officer",
        "name": "Chief Marketing Officer",
        "professional_field_id": "marketing_communications",
        "subfield_id": "marketing_strategy_operations",
        "description": "Leads enterprise-wide marketing strategy, brand direction, and growth.",
        "is_active": True,
    },
])



# ============================================================
# HUMAN RESOURCES — ALL SIX SUBFIELDS
# ============================================================

CANONICAL_ROLES.extend([

    # 1. TALENT ACQUISITION & RECRUITMENT

    {
        "id": "recruiter",
        "name": "Recruiter",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Sources, screens, and recruits candidates for organizational vacancies.",
        "is_active": True,
    },
    {
        "id": "talent_acquisition_specialist",
        "name": "Talent Acquisition Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Manages candidate sourcing, screening, and recruitment coordination.",
        "is_active": True,
    },
    {
        "id": "talent_acquisition_manager",
        "name": "Talent Acquisition Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Leads recruitment strategy, hiring operations, and talent acquisition teams.",
        "is_active": True,
    },
    {
        "id": "technical_recruiter",
        "name": "Technical Recruiter",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Recruits candidates for technology, engineering, and technical positions.",
        "is_active": True,
    },
    {
        "id": "executive_recruiter",
        "name": "Executive Recruiter",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Sources and recruits senior leaders and executive-level candidates.",
        "is_active": True,
    },
    {
        "id": "recruitment_coordinator",
        "name": "Recruitment Coordinator",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Coordinates interviews, candidate communication, and recruitment administration.",
        "is_active": True,
    },
    {
        "id": "sourcing_specialist",
        "name": "Talent Sourcing Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Identifies and engages potential candidates through sourcing channels.",
        "is_active": True,
    },
    {
        "id": "recruitment_manager",
        "name": "Recruitment Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Manages recruitment operations, hiring teams, and staffing delivery.",
        "is_active": True,
    },
    {
        "id": "head_of_talent_acquisition",
        "name": "Head of Talent Acquisition",
        "professional_field_id": "human_resources",
        "subfield_id": "talent_acquisition_recruitment",
        "description": "Oversees organization-wide talent acquisition strategy and hiring performance.",
        "is_active": True,
    },

    # 2. HR OPERATIONS & ADMINISTRATION

    {
        "id": "hr_executive",
        "name": "HR Executive",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_operations_administration",
        "description": "Handles day-to-day human resources administration and employee support.",
        "is_active": True,
    },
    {
        "id": "hr_generalist",
        "name": "HR Generalist",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_operations_administration",
        "description": "Supports recruitment, employee relations, HR administration, and workforce processes.",
        "is_active": True,
    },
    {
        "id": "hr_manager",
        "name": "HR Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_operations_administration",
        "description": "Manages HR operations, policies, employee administration, and HR teams.",
        "is_active": True,
    },
    {
        "id": "hr_operations_specialist",
        "name": "HR Operations Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_operations_administration",
        "description": "Manages employee lifecycle processes, HR systems, and operational administration.",
        "is_active": True,
    },
    {
        "id": "hr_administrator",
        "name": "HR Administrator",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_operations_administration",
        "description": "Maintains employee records, documentation, and routine HR administration.",
        "is_active": True,
    },
    {
        "id": "hr_coordinator",
        "name": "HR Coordinator",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_operations_administration",
        "description": "Coordinates HR activities, employee documentation, and internal processes.",
        "is_active": True,
    },
    {
        "id": "hr_director",
        "name": "HR Director",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_operations_administration",
        "description": "Directs HR operations, workforce policies, and people management strategy.",
        "is_active": True,
    },

    # 3. LEARNING & DEVELOPMENT

    {
        "id": "learning_development_specialist",
        "name": "Learning & Development Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Designs and coordinates employee learning and development initiatives.",
        "is_active": True,
    },
    {
        "id": "learning_development_manager",
        "name": "Learning & Development Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Leads organizational learning programs and employee development strategy.",
        "is_active": True,
    },
    {
        "id": "training_manager",
        "name": "Training Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Manages employee training programs, trainers, and training delivery.",
        "is_active": True,
    },
    {
        "id": "training_coordinator",
        "name": "Training Coordinator",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Coordinates training schedules, logistics, materials, and participation.",
        "is_active": True,
    },
    {
        "id": "learning_consultant",
        "name": "Learning Consultant",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Advises organizations on learning needs and employee development solutions.",
        "is_active": True,
    },
    {
        "id": "organizational_development_specialist",
        "name": "Organizational Development Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Supports organizational effectiveness, workforce development, and change initiatives.",
        "is_active": True,
    },
    {
        "id": "leadership_development_manager",
        "name": "Leadership Development Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Develops leadership capabilities and management development programs.",
        "is_active": True,
    },
    {
        "id": "learning_development_director",
        "name": "Learning & Development Director",
        "professional_field_id": "human_resources",
        "subfield_id": "learning_development",
        "description": "Directs enterprise learning strategy and employee capability development.",
        "is_active": True,
    },

    # 4. COMPENSATION, BENEFITS & PAYROLL

    {
        "id": "compensation_benefits_specialist",
        "name": "Compensation & Benefits Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Administers employee compensation structures and benefits programs.",
        "is_active": True,
    },
    {
        "id": "compensation_analyst",
        "name": "Compensation Analyst",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Analyzes salary structures, pay benchmarks, and compensation data.",
        "is_active": True,
    },
    {
        "id": "compensation_manager",
        "name": "Compensation Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Manages compensation policies, salary frameworks, and pay programs.",
        "is_active": True,
    },
    {
        "id": "benefits_administrator",
        "name": "Benefits Administrator",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Administers employee benefits, enrollment, and benefits-related records.",
        "is_active": True,
    },
    {
        "id": "benefits_manager",
        "name": "Benefits Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Oversees employee benefits programs, vendors, and benefits policies.",
        "is_active": True,
    },
    {
        "id": "payroll_specialist",
        "name": "Payroll Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Processes employee payroll and maintains accurate payroll records.",
        "is_active": True,
    },
    {
        "id": "payroll_manager",
        "name": "Payroll Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Manages payroll operations, compliance, and payroll administration teams.",
        "is_active": True,
    },
    {
        "id": "compensation_benefits_manager",
        "name": "Compensation & Benefits Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "compensation_benefits_payroll",
        "description": "Leads total rewards strategy, compensation, and employee benefits.",
        "is_active": True,
    },

    # 5. EMPLOYEE RELATIONS & ENGAGEMENT

    {
        "id": "employee_relations_specialist",
        "name": "Employee Relations Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Handles employee relations matters, workplace concerns, and HR guidance.",
        "is_active": True,
    },
    {
        "id": "employee_relations_manager",
        "name": "Employee Relations Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Leads employee relations policies, case management, and workplace practices.",
        "is_active": True,
    },
    {
        "id": "employee_engagement_specialist",
        "name": "Employee Engagement Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Develops initiatives to improve employee engagement and workplace participation.",
        "is_active": True,
    },
    {
        "id": "employee_engagement_manager",
        "name": "Employee Engagement Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Leads employee engagement programs and measures workforce sentiment.",
        "is_active": True,
    },
    {
        "id": "employee_experience_specialist",
        "name": "Employee Experience Specialist",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Improves employee experiences across workplace and employment lifecycle processes.",
        "is_active": True,
    },
    {
        "id": "industrial_relations_manager",
        "name": "Industrial Relations Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Manages labor relations, workforce negotiations, and industrial relations matters.",
        "is_active": True,
    },
    {
        "id": "employee_experience_manager",
        "name": "Employee Experience Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Manages employee experience initiatives and workplace engagement programs.",
        "is_active": True,
    },
    {
        "id": "employee_relations_director",
        "name": "Employee Relations Director",
        "professional_field_id": "human_resources",
        "subfield_id": "employee_relations_engagement",
        "description": "Directs employee relations strategy and organizational workplace policies.",
        "is_active": True,
    },

    # 6. HR STRATEGY & BUSINESS PARTNERING

    {
        "id": "hr_business_partner",
        "name": "HR Business Partner",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Partners with business leaders to align HR support with organizational needs.",
        "is_active": True,
    },
    {
        "id": "senior_hr_business_partner",
        "name": "Senior HR Business Partner",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Provides strategic HR partnership and workforce guidance to senior business leaders.",
        "is_active": True,
    },
    {
        "id": "hr_strategy_manager",
        "name": "HR Strategy Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Develops HR strategies aligned with organizational goals and workforce priorities.",
        "is_active": True,
    },
    {
        "id": "people_strategy_manager",
        "name": "People Strategy Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Leads people strategy, workforce planning, and organizational people initiatives.",
        "is_active": True,
    },
    {
        "id": "workforce_planning_manager",
        "name": "Workforce Planning Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Leads workforce planning, talent forecasting, and organizational capacity planning.",
        "is_active": True,
    },
    {
        "id": "organizational_development_manager",
        "name": "Organizational Development Manager",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Leads organizational development, effectiveness, and transformation initiatives.",
        "is_active": True,
    },
    {
        "id": "chief_human_resources_officer",
        "name": "Chief Human Resources Officer",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Leads enterprise-wide human resources and people strategy.",
        "is_active": True,
    },
    {
        "id": "vice_president_human_resources",
        "name": "Vice President of Human Resources",
        "professional_field_id": "human_resources",
        "subfield_id": "hr_strategy_business_partnering",
        "description": "Provides executive leadership for human resources strategy and operations.",
        "is_active": True,
    },
])



# ============================================================
# OPERATIONS & ADMINISTRATION — ALL SIX SUBFIELDS
# ============================================================

CANONICAL_ROLES.extend([

    # 1. BUSINESS OPERATIONS & PROCESS MANAGEMENT

    {
        "id": "business_operations_manager",
        "name": "Business Operations Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Manages daily business operations, resources, and operational performance.",
        "is_active": True,
    },
    {
        "id": "operations_manager",
        "name": "Operations Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Oversees operational activities, teams, and service delivery.",
        "is_active": True,
    },
    {
        "id": "business_operations_analyst",
        "name": "Business Operations Analyst",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Analyzes business processes and operational performance to identify improvements.",
        "is_active": True,
    },
    {
        "id": "operations_coordinator",
        "name": "Operations Coordinator",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Coordinates daily operations, resources, schedules, and cross-functional activities.",
        "is_active": True,
    },
    {
        "id": "business_operations_director",
        "name": "Business Operations Director",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Directs business operations and organizational operational performance.",
        "is_active": True,
    },
    {
        "id": "operations_executive",
        "name": "Operations Executive",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Executes and monitors routine business operations and administrative processes.",
        "is_active": True,
    },
    {
        "id": "business_operations_specialist",
        "name": "Business Operations Specialist",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Supports operational planning, process coordination, and business execution.",
        "is_active": True,
    },
    {
        "id": "head_of_operations",
        "name": "Head of Operations",
        "professional_field_id": "operations_administration",
        "subfield_id": "business_operations_process_management",
        "description": "Leads organization-wide operational functions and business execution.",
        "is_active": True,
    },

    # 2. OFFICE ADMINISTRATION & EXECUTIVE SUPPORT

    {
        "id": "administrative_assistant",
        "name": "Administrative Assistant",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Provides administrative support, documentation, and office coordination.",
        "is_active": True,
    },
    {
        "id": "office_administrator",
        "name": "Office Administrator",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Manages office administration, records, supplies, and routine office activities.",
        "is_active": True,
    },
    {
        "id": "office_manager",
        "name": "Office Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Oversees office operations, administrative staff, and workplace resources.",
        "is_active": True,
    },
    {
        "id": "executive_assistant",
        "name": "Executive Assistant",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Provides high-level administrative and scheduling support to executives.",
        "is_active": True,
    },
    {
        "id": "personal_assistant",
        "name": "Personal Assistant",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Provides organizational, scheduling, and administrative support to an individual.",
        "is_active": True,
    },
    {
        "id": "administration_manager",
        "name": "Administration Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Manages administrative functions, office policies, and support teams.",
        "is_active": True,
    },
    {
        "id": "administrative_coordinator",
        "name": "Administrative Coordinator",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Coordinates administrative workflows, meetings, records, and office services.",
        "is_active": True,
    },
    {
        "id": "executive_administrator",
        "name": "Executive Administrator",
        "professional_field_id": "operations_administration",
        "subfield_id": "office_administration_executive_support",
        "description": "Supports senior leadership through executive administration and office coordination.",
        "is_active": True,
    },

    # 3. SUPPLY CHAIN, LOGISTICS & DISTRIBUTION

    {
        "id": "supply_chain_manager",
        "name": "Supply Chain Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Manages end-to-end supply chain planning, sourcing, and distribution.",
        "is_active": True,
    },
    {
        "id": "logistics_manager",
        "name": "Logistics Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Oversees transportation, logistics operations, and goods movement.",
        "is_active": True,
    },
    {
        "id": "logistics_coordinator",
        "name": "Logistics Coordinator",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Coordinates shipments, transport schedules, and logistics documentation.",
        "is_active": True,
    },
    {
        "id": "distribution_manager",
        "name": "Distribution Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Manages distribution networks, delivery operations, and distribution teams.",
        "is_active": True,
    },
    {
        "id": "warehouse_manager",
        "name": "Warehouse Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Oversees warehouse operations, storage, inventory handling, and staff.",
        "is_active": True,
    },
    {
        "id": "inventory_controller",
        "name": "Inventory Controller",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Monitors inventory levels, stock accuracy, and inventory movements.",
        "is_active": True,
    },
    {
        "id": "transportation_manager",
        "name": "Transportation Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Manages transportation planning, carriers, and delivery performance.",
        "is_active": True,
    },
    {
        "id": "fleet_manager",
        "name": "Fleet Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "supply_chain_logistics_distribution",
        "description": "Manages vehicle fleets, fleet maintenance, utilization, and compliance.",
        "is_active": True,
    },

    # 4. PROCUREMENT & PURCHASING

    {
        "id": "procurement_specialist",
        "name": "Procurement Specialist",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Sources suppliers and manages purchasing activities and procurement documentation.",
        "is_active": True,
    },
    {
        "id": "procurement_manager",
        "name": "Procurement Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Leads procurement strategy, supplier selection, and purchasing operations.",
        "is_active": True,
    },
    {
        "id": "purchasing_manager",
        "name": "Purchasing Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Manages purchasing activities, purchase orders, and supplier relationships.",
        "is_active": True,
    },
    {
        "id": "procurement_officer",
        "name": "Procurement Officer",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Executes procurement procedures and coordinates purchasing requirements.",
        "is_active": True,
    },
    {
        "id": "buyer",
        "name": "Buyer",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Purchases goods and services according to cost, quality, and delivery requirements.",
        "is_active": True,
    },
    {
        "id": "strategic_sourcing_manager",
        "name": "Strategic Sourcing Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Develops strategic sourcing plans and optimizes supplier relationships and costs.",
        "is_active": True,
    },
    {
        "id": "vendor_manager",
        "name": "Vendor Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Manages vendor performance, contracts, and supplier relationships.",
        "is_active": True,
    },
    {
        "id": "procurement_director",
        "name": "Procurement Director",
        "professional_field_id": "operations_administration",
        "subfield_id": "procurement_purchasing",
        "description": "Directs organization-wide procurement strategy and purchasing governance.",
        "is_active": True,
    },

    # 5. FACILITIES & WORKPLACE MANAGEMENT

    {
        "id": "facilities_manager",
        "name": "Facilities Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Manages building facilities, maintenance services, and workplace infrastructure.",
        "is_active": True,
    },
    {
        "id": "facilities_coordinator",
        "name": "Facilities Coordinator",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Coordinates facilities services, maintenance requests, and workplace resources.",
        "is_active": True,
    },
    {
        "id": "workplace_manager",
        "name": "Workplace Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Manages workplace services, office environments, and employee facilities.",
        "is_active": True,
    },
    {
        "id": "building_manager",
        "name": "Building Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Oversees building operations, maintenance, safety, and service providers.",
        "is_active": True,
    },
    {
        "id": "workplace_experience_manager",
        "name": "Workplace Experience Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Improves workplace services and the day-to-day employee office experience.",
        "is_active": True,
    },
    {
        "id": "facilities_operations_manager",
        "name": "Facilities Operations Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Leads facilities operations, service delivery, and maintenance coordination.",
        "is_active": True,
    },
    {
        "id": "facilities_director",
        "name": "Facilities Director",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Directs facilities strategy, building operations, and workplace infrastructure.",
        "is_active": True,
    },
    {
        "id": "workplace_services_manager",
        "name": "Workplace Services Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "facilities_workplace_management",
        "description": "Manages workplace support services, vendors, and employee facilities.",
        "is_active": True,
    },

    # 6. PROCESS IMPROVEMENT & BUSINESS EXCELLENCE

    {
        "id": "process_improvement_manager",
        "name": "Process Improvement Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Leads initiatives to improve business processes, efficiency, and performance.",
        "is_active": True,
    },
    {
        "id": "business_excellence_manager",
        "name": "Business Excellence Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Leads business excellence programs and organizational performance improvement.",
        "is_active": True,
    },
    {
        "id": "process_improvement_specialist",
        "name": "Process Improvement Specialist",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Identifies process inefficiencies and implements operational improvements.",
        "is_active": True,
    },
    {
        "id": "operational_excellence_manager",
        "name": "Operational Excellence Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Drives operational excellence through standardized processes and performance initiatives.",
        "is_active": True,
    },
    {
        "id": "lean_six_sigma_manager",
        "name": "Lean Six Sigma Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Leads Lean Six Sigma initiatives to reduce waste and improve process quality.",
        "is_active": True,
    },
    {
        "id": "business_process_manager",
        "name": "Business Process Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Manages business process design, documentation, governance, and optimization.",
        "is_active": True,
    },
    {
        "id": "business_process_consultant",
        "name": "Business Process Consultant",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Advises organizations on process redesign and operational effectiveness.",
        "is_active": True,
    },
    {
        "id": "continuous_improvement_manager",
        "name": "Continuous Improvement Manager",
        "professional_field_id": "operations_administration",
        "subfield_id": "process_improvement_business_excellence",
        "description": "Manages continuous improvement programs across business operations.",
        "is_active": True,
    },

])


# ============================================================
# CUSTOMER SUPPORT & BPO — CONSOLIDATED CANONICAL ROLE CATALOGUE
# 6 subfields | 66 canonical roles
# ============================================================

CANONICAL_ROLES.extend([

    # 1. CUSTOMER SERVICE & CUSTOMER CARE
    {
        "id": "customer_service_executive",
        "name": "Customer Service Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Handles customer inquiries, service requests, complaints, and routine assistance.",
        "is_active": True,
    },
    {
        "id": "customer_service_representative",
        "name": "Customer Service Representative",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Assists customers with questions, complaints, and service-related needs.",
        "is_active": True,
    },
    {
        "id": "customer_support_agent",
        "name": "Customer Support Agent",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Provides customer assistance through phone, email, chat, and other support channels.",
        "is_active": True,
    },
    {
        "id": "customer_support_representative",
        "name": "Customer Support Representative",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Responds to customer questions and resolves routine product and service issues.",
        "is_active": True,
    },
    {
        "id": "customer_care_executive",
        "name": "Customer Care Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Provides customer care and maintains positive customer interactions.",
        "is_active": True,
    },
    {
        "id": "customer_service_advisor",
        "name": "Customer Service Advisor",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Advises customers and helps resolve service and account-related queries.",
        "is_active": True,
    },
    {
        "id": "customer_service_associate",
        "name": "Customer Service Associate",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Supports customers with routine inquiries, requests, and service transactions.",
        "is_active": True,
    },
    {
        "id": "customer_service_coordinator",
        "name": "Customer Service Coordinator",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Coordinates customer requests and service activities across internal teams.",
        "is_active": True,
    },
    {
        "id": "customer_service_specialist",
        "name": "Customer Service Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Handles specialized customer inquiries and complex service-related issues.",
        "is_active": True,
    },
    {
        "id": "customer_service_supervisor",
        "name": "Customer Service Supervisor",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Supervises customer service representatives and daily service activities.",
        "is_active": True,
    },
    {
        "id": "customer_service_manager",
        "name": "Customer Service Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_service_customer_care",
        "description": "Manages customer service teams, service quality, and customer support operations.",
        "is_active": True,
    },

    # 2. CONTACT CENTER & CALL CENTER OPERATIONS
    {
        "id": "call_center_agent",
        "name": "Call Center Agent",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Handles inbound and outbound customer calls in a call center.",
        "is_active": True,
    },
    {
        "id": "inbound_call_agent",
        "name": "Inbound Call Center Agent",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Handles incoming customer calls, inquiries, and service requests.",
        "is_active": True,
    },
    {
        "id": "outbound_call_agent",
        "name": "Outbound Call Center Agent",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Makes outbound calls for customer follow-ups, surveys, and service or sales campaigns.",
        "is_active": True,
    },
    {
        "id": "contact_center_executive",
        "name": "Contact Center Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Handles customer interactions through contact center channels.",
        "is_active": True,
    },
    {
        "id": "call_center_team_leader",
        "name": "Call Center Team Leader",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Leads call center agents and monitors team performance and service delivery.",
        "is_active": True,
    },
    {
        "id": "call_center_supervisor",
        "name": "Call Center Supervisor",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Supervises call center agents and daily operational performance.",
        "is_active": True,
    },
    {
        "id": "contact_center_manager",
        "name": "Contact Center Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Manages contact center staffing, service delivery, and operational performance.",
        "is_active": True,
    },
    {
        "id": "call_center_manager",
        "name": "Call Center Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Leads call center operations, teams, and customer interaction performance.",
        "is_active": True,
    },
    {
        "id": "workforce_management_analyst",
        "name": "Workforce Management Analyst",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Forecasts contact volumes and plans staffing, capacity, and agent schedules.",
        "is_active": True,
    },
    {
        "id": "contact_center_trainer",
        "name": "Contact Center Trainer",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Trains contact center employees on service procedures and communication skills.",
        "is_active": True,
    },
    {
        "id": "contact_center_director",
        "name": "Contact Center Director",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "contact_center_call_center_operations",
        "description": "Directs contact center strategy, workforce operations, and service performance.",
        "is_active": True,
    },

    # 3. TECHNICAL & PRODUCT SUPPORT
    {
        "id": "technical_support_analyst",
        "name": "Technical Support Analyst",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Diagnoses technical issues and assists users with technology and product problems.",
        "is_active": True,
    },
    {
        "id": "product_support_specialist",
        "name": "Product Support Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Assists customers with product functionality, configuration, and troubleshooting.",
        "is_active": True,
    },
    {
        "id": "product_support_manager",
        "name": "Product Support Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Manages product support teams and customer technical assistance.",
        "is_active": True,
    },
    {
        "id": "application_support_specialist",
        "name": "Application Support Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Supports application users and resolves software-related functional issues.",
        "is_active": True,
    },
    {
        "id": "software_support_engineer",
        "name": "Software Support Engineer",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Investigates software problems and provides technical product support.",
        "is_active": True,
    },
    {
        "id": "hardware_support_specialist",
        "name": "Hardware Support Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Diagnoses hardware problems and assists customers with hardware-related issues.",
        "is_active": True,
    },
    {
        "id": "product_support_analyst",
        "name": "Product Support Analyst",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Analyzes product support issues, usage problems, and recurring incidents.",
        "is_active": True,
    },
    {
        "id": "technical_support_manager",
        "name": "Technical Support Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Leads technical support teams and manages customer technical service delivery.",
        "is_active": True,
    },
    {
    "id": "product_support_coordinator",
    "name": "Product Support Coordinator",
    "professional_field_id": "customer_support_bpo",
    "subfield_id": "technical_product_support",
    "description": "Coordinates product support requests, tracks technical issues, and assists customers with support processes.",
    "is_active": True,
    },
    {
        "id": "service_desk_analyst",
        "name": "Service Desk Analyst",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Handles IT service requests, incidents, and user support through a service desk.",
        "is_active": True,
    },
    {
        "id": "help_desk_manager",
        "name": "Help Desk Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "technical_product_support",
        "description": "Manages help desk staff, technical support workflows, and service standards.",
        "is_active": True,
    },

    # 4. CUSTOMER SUCCESS & CLIENT SERVICES
    {
        "id": "customer_success_manager",
        "name": "Customer Success Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Builds customer relationships and helps customers achieve value from products and services.",
        "is_active": True,
    },
    {
        "id": "customer_success_specialist",
        "name": "Customer Success Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Supports customer onboarding, adoption, engagement, and retention.",
        "is_active": True,
    },
    {
        "id": "customer_success_director",
        "name": "Customer Success Director",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Directs customer success strategy, teams, and retention initiatives.",
        "is_active": True,
    },
    {
    "id": "client_services_coordinator",
    "name": "Client Services Coordinator",
    "professional_field_id": "customer_support_bpo",
    "subfield_id": "customer_success_client_services",
    "description": "Coordinates client requests, service delivery, and communication between clients and internal teams.",
    "is_active": True,
    },
    {
        "id": "client_services_executive",
        "name": "Client Services Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Coordinates client requests and supports day-to-day client service activities.",
        "is_active": True,
    },
    {
    "id": "customer_success_relationship_specialist",
    "name": "Customer Success Relationship Specialist",
    "professional_field_id": "customer_support_bpo",
    "subfield_id": "customer_success_client_services",
    "description": "Builds customer relationships and supports customer engagement, adoption, and retention.",
    "is_active": True,
    },
    {
        "id": "customer_onboarding_specialist",
        "name": "Customer Onboarding Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Guides new customers through product setup and onboarding processes.",
        "is_active": True,
    },
    {
        "id": "customer_retention_manager",
        "name": "Customer Retention Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Develops strategies to improve customer loyalty and reduce customer churn.",
        "is_active": True,
    },
    {
        "id": "customer_success_associate",
        "name": "Customer Success Associate",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Assists with customer adoption, account engagement, and success activities.",
        "is_active": True,
    },
    {
        "id": "implementation_specialist",
        "name": "Implementation Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Coordinates customer implementation, product setup, and deployment activities.",
        "is_active": True,
    },
    {
        "id": "customer_onboarding_manager",
        "name": "Customer Onboarding Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_success_client_services",
        "description": "Manages customer onboarding programs and initial product adoption.",
        "is_active": True,
    },

    # 5. BACK-OFFICE & TRANSACTION PROCESSING
    {
        "id": "back_office_executive",
        "name": "Back Office Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Performs administrative and transaction-processing activities supporting business operations.",
        "is_active": True,
    },
    {
        "id": "back_office_associate",
        "name": "Back Office Associate",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Processes business documentation, records, and routine operational transactions.",
        "is_active": True,
    },
    {
        "id": "transaction_processing_specialist",
        "name": "Transaction Processing Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Processes and verifies customer and business transactions accurately.",
        "is_active": True,
    },
    {
        "id": "back_office_manager",
        "name": "Back Office Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Manages back-office teams, transaction workflows, and processing operations.",
        "is_active": True,
    },
    {
        "id": "data_processing_executive",
        "name": "Data Processing Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Processes and maintains business data and transaction records.",
        "is_active": True,
    },
    {
        "id": "claims_processing_specialist",
        "name": "Claims Processing Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Reviews and processes customer claims and supporting documentation.",
        "is_active": True,
    },
    {
        "id": "order_processing_specialist",
        "name": "Order Processing Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Processes customer orders and coordinates order documentation and fulfillment.",
        "is_active": True,
    },
    {
        "id": "transaction_processing_manager",
        "name": "Transaction Processing Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Oversees transaction processing teams, controls, and service quality.",
        "is_active": True,
    },
    {
        "id": "data_entry_operator",
        "name": "Data Entry Operator",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Enters, updates, and validates business and customer information in systems.",
        "is_active": True,
    },
    {
        "id": "mis_executive",
        "name": "MIS Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Prepares operational reports and maintains management information records.",
        "is_active": True,
    },
    {
        "id": "billing_executive",
        "name": "Billing Executive",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "back_office_transaction_processing",
        "description": "Processes customer billing, invoices, and related account documentation.",
        "is_active": True,
    },

    # 6. CUSTOMER EXPERIENCE, QUALITY & ESCALATIONS
    {
        "id": "customer_experience_specialist",
        "name": "Customer Experience Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Evaluates customer journeys and supports improvements to customer experiences.",
        "is_active": True,
    },
    {
        "id": "customer_experience_manager",
        "name": "Customer Experience Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Leads customer experience programs and customer journey improvements.",
        "is_active": True,
    },
    {
        "id": "customer_quality_analyst",
        "name": "Customer Quality Analyst",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Evaluates customer interactions against service quality standards.",
        "is_active": True,
    },
    {
        "id": "quality_assurance_team_leader",
        "name": "Customer Service Quality Team Leader",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Leads quality monitoring teams and customer service improvement activities.",
        "is_active": True,
    },
    {
        "id": "customer_escalation_specialist",
        "name": "Customer Escalation Specialist",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Handles complex customer complaints and escalated service issues.",
        "is_active": True,
    },
    {
        "id": "customer_escalations_manager",
        "name": "Customer Escalations Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Manages escalated customer cases and complaint resolution processes.",
        "is_active": True,
    },
    {
        "id": "customer_experience_analyst",
        "name": "Customer Experience Analyst",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Analyzes customer feedback, satisfaction, and experience metrics.",
        "is_active": True,
    },
    {
        "id": "customer_quality_manager",
        "name": "Customer Quality Manager",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Manages customer service quality standards, audits, and improvement programs.",
        "is_active": True,
    },
    {
    "id": "customer_service_quality_analyst",
    "name": "Customer Service Quality Analyst",
    "professional_field_id": "customer_support_bpo",
    "subfield_id": "customer_experience_quality_escalations",
    "description": "Evaluates customer service interactions and monitors compliance with customer experience standards.",
    "is_active": True,
    },
    {
        "id": "quality_auditor",
        "name": "Customer Service Quality Auditor",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Audits customer service interactions, documentation, and process adherence.",
        "is_active": True,
    },
    {
        "id": "customer_feedback_analyst",
        "name": "Customer Feedback Analyst",
        "professional_field_id": "customer_support_bpo",
        "subfield_id": "customer_experience_quality_escalations",
        "description": "Analyzes customer feedback, survey results, and satisfaction trends.",
        "is_active": True,
    },

])


CANONICAL_ROLES.extend([
    # ============================================================
    # PRODUCT & PROJECT MANAGEMENT
    # ============================================================

    # 1. Product Management
    {
        "id": "product_manager",
        "name": "Product Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Defines product direction, prioritizes features, and coordinates product development to meet customer and business needs.",
        "is_active": True,
    },
    {
        "id": "senior_product_manager",
        "name": "Senior Product Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Leads product strategy, roadmap planning, and cross-functional execution for complex products or product areas.",
        "is_active": True,
    },
    {
        "id": "associate_product_manager",
        "name": "Associate Product Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Supports product planning, requirement definition, prioritization, and coordination of product development activities.",
        "is_active": True,
    },
    {
        "id": "junior_product_manager",
        "name": "Junior Product Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Assists with product research, feature planning, backlog coordination, and monitoring product performance.",
        "is_active": True,
    },
    {
        "id": "technical_product_manager",
        "name": "Technical Product Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Manages technical products by translating business requirements into technical priorities and coordinating engineering teams.",
        "is_active": True,
    },
    {
        "id": "digital_product_manager",
        "name": "Digital Product Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Manages digital products and platforms, overseeing their strategy, development, user experience, and performance.",
        "is_active": True,
    },
    {
        "id": "product_owner",
        "name": "Product Owner",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Owns and prioritizes the product backlog, clarifies requirements, and represents stakeholder needs during product development.",
        "is_active": True,
    },
    {
        "id": "chief_product_officer",
        "name": "Chief Product Officer",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_management",
        "description": "Leads the organization's overall product vision, strategy, portfolio direction, and product management function.",
        "is_active": True,
    },

    # 2. Project Management
    {
        "id": "project_manager",
        "name": "Project Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Plans and manages projects, coordinating scope, schedules, budgets, resources, risks, and stakeholder expectations.",
        "is_active": True,
    },
    {
        "id": "senior_project_manager",
        "name": "Senior Project Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Leads complex projects and manages delivery performance, project governance, risks, budgets, and senior stakeholders.",
        "is_active": True,
    },
    {
        "id": "associate_project_manager",
        "name": "Associate Project Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Supports project planning, execution tracking, resource coordination, reporting, and stakeholder communication.",
        "is_active": True,
    },
    {
        "id": "junior_project_manager",
        "name": "Junior Project Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Assists with project schedules, task coordination, progress tracking, documentation, and delivery activities.",
        "is_active": True,
    },
    {
        "id": "it_project_manager",
        "name": "IT Project Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Manages information technology projects involving software, infrastructure, systems implementation, and technical delivery.",
        "is_active": True,
    },
    {
        "id": "business_project_manager",
        "name": "Business Project Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Leads business-focused projects involving organizational processes, operational improvements, and business transformation.",
        "is_active": True,
    },
    {
        "id": "project_coordinator",
        "name": "Project Coordinator",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Coordinates project activities, schedules, documentation, meetings, reporting, and communication across project teams.",
        "is_active": True,
    },
    {
        "id": "project_director",
        "name": "Project Director",
        "professional_field_id": "product_project_management",
        "subfield_id": "project_management",
        "description": "Provides strategic oversight of major projects, directing delivery teams, governance, budgets, and executive stakeholder relationships.",
        "is_active": True,
    },

    # 3. Program Management
    {
        "id": "program_manager",
        "name": "Program Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Coordinates related projects and initiatives to achieve strategic business objectives and program outcomes.",
        "is_active": True,
    },
    {
        "id": "senior_program_manager",
        "name": "Senior Program Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Leads large and complex programs, overseeing multiple projects, dependencies, resources, risks, and strategic outcomes.",
        "is_active": True,
    },
    {
        "id": "associate_program_manager",
        "name": "Associate Program Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Supports program planning, project coordination, progress monitoring, reporting, and stakeholder engagement.",
        "is_active": True,
    },
    {
        "id": "technical_program_manager",
        "name": "Technical Program Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Coordinates complex technical programs across engineering teams, managing dependencies, delivery milestones, and technical risks.",
        "is_active": True,
    },
    {
        "id": "business_program_manager",
        "name": "Business Program Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Leads business programs involving strategic initiatives, operational improvements, organizational change, and cross-functional delivery.",
        "is_active": True,
    },
    {
        "id": "program_coordinator",
        "name": "Program Coordinator",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Coordinates program schedules, documentation, communications, reporting, and administrative activities across related projects.",
        "is_active": True,
    },
    {
        "id": "program_director",
        "name": "Program Director",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Directs strategic programs, overseeing program managers, investment priorities, governance, and achievement of organizational outcomes.",
        "is_active": True,
    },
    {
        "id": "head_of_program_management",
        "name": "Head of Program Management",
        "professional_field_id": "product_project_management",
        "subfield_id": "program_management",
        "description": "Leads the program management function, establishing delivery standards, governance practices, and strategic program oversight.",
        "is_active": True,
    },

    # 4. Portfolio & PMO Management
    {
        "id": "project_portfolio_manager",
        "name": "Project Portfolio Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Oversees a portfolio of projects, aligning priorities, resources, investments, and delivery outcomes with organizational strategy.",
        "is_active": True,
    },
    {
        "id": "portfolio_management_office_manager",
        "name": "Portfolio Management Office Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Manages portfolio management office activities, including portfolio governance, prioritization, performance reporting, and resource oversight.",
        "is_active": True,
    },
    {
        "id": "pmo_manager",
        "name": "PMO Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Manages the project management office, establishing project standards, governance frameworks, reporting, and delivery controls.",
        "is_active": True,
    },
    {
        "id": "pmo_analyst",
        "name": "PMO Analyst",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Analyzes project and portfolio performance data, prepares management reports, and supports PMO governance and planning.",
        "is_active": True,
    },
    {
        "id": "pmo_coordinator",
        "name": "PMO Coordinator",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Coordinates PMO administration, project reporting, governance documentation, meetings, and project management processes.",
        "is_active": True,
    },
    {
        "id": "project_portfolio_analyst",
        "name": "Project Portfolio Analyst",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Evaluates project portfolios, analyzes investment and delivery performance, and supports portfolio planning and decision-making.",
        "is_active": True,
    },
    {
        "id": "portfolio_governance_manager",
        "name": "Portfolio Governance Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Establishes and oversees portfolio governance, investment controls, prioritization frameworks, and strategic alignment.",
        "is_active": True,
    },
    {
        "id": "head_of_pmo",
        "name": "Head of PMO",
        "professional_field_id": "product_project_management",
        "subfield_id": "portfolio_pmo_management",
        "description": "Leads the project management office function, directing project governance, delivery standards, portfolio reporting, and oversight.",
        "is_active": True,
    },

    # 5. Agile & Scrum Management
    {
        "id": "scrum_master",
        "name": "Scrum Master",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Facilitates Scrum practices, removes delivery impediments, and supports teams in applying Agile principles.",
        "is_active": True,
    },
    {
        "id": "senior_scrum_master",
        "name": "Senior Scrum Master",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Guides multiple Scrum teams, improves Agile delivery practices, and coaches teams and stakeholders on effective collaboration.",
        "is_active": True,
    },
    {
        "id": "agile_coach",
        "name": "Agile Coach",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Coaches teams and leaders in Agile methods, continuous improvement, collaboration, and effective product delivery.",
        "is_active": True,
    },
    {
        "id": "enterprise_agile_coach",
        "name": "Enterprise Agile Coach",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Leads enterprise-level Agile coaching and transformation, helping organizations scale Agile practices across departments.",
        "is_active": True,
    },
    {
        "id": "agile_delivery_manager",
        "name": "Agile Delivery Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Oversees Agile delivery teams, managing delivery flow, dependencies, risks, and continuous improvement.",
        "is_active": True,
    },
    {
        "id": "release_train_engineer",
        "name": "Release Train Engineer",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Facilitates large-scale Agile release trains, coordinating planning events, dependencies, risks, and delivery across teams.",
        "is_active": True,
    },
    {
        "id": "agile_project_manager",
        "name": "Agile Project Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Manages project delivery using Agile methodologies, coordinating iterative planning, team collaboration, and stakeholder feedback.",
        "is_active": True,
    },
    {
        "id": "agile_transformation_manager",
        "name": "Agile Transformation Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "agile_scrum_management",
        "description": "Leads organizational Agile transformation initiatives, improving delivery models, team structures, processes, and governance.",
        "is_active": True,
    },

    # 6. Product Operations & Strategy
    {
        "id": "product_operations_manager",
        "name": "Product Operations Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Establishes product operations processes, tools, reporting, and workflows to improve product team effectiveness.",
        "is_active": True,
    },
    {
        "id": "product_operations_specialist",
        "name": "Product Operations Specialist",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Supports product teams through operational coordination, documentation, tooling, data collection, and process improvement.",
        "is_active": True,
    },
    {
        "id": "product_operations_analyst",
        "name": "Product Operations Analyst",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Analyzes product operations data, monitors workflows, and provides insights to improve product planning and execution.",
        "is_active": True,
    },
    {
        "id": "product_strategy_manager",
        "name": "Product Strategy Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Develops product strategies, evaluates market opportunities, and aligns product investments with long-term business objectives.",
        "is_active": True,
    },
    {
        "id": "product_strategy_analyst",
        "name": "Product Strategy Analyst",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Researches markets, competitors, and product performance to support strategic product decisions and planning.",
        "is_active": True,
    },
    {
        "id": "product_management_director",
        "name": "Director of Product Management",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Leads product management teams and establishes product strategy, organizational practices, and portfolio priorities.",
        "is_active": True,
    },
    {
        "id": "head_of_product_operations",
        "name": "Head of Product Operations",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Leads the product operations function, improving product team processes, operating models, tools, and performance measurement.",
        "is_active": True,
    },
    {
        "id": "product_planning_manager",
        "name": "Product Planning Manager",
        "professional_field_id": "product_project_management",
        "subfield_id": "product_operations_strategy",
        "description": "Coordinates product planning cycles, roadmap development, resource alignment, and cross-functional product priorities.",
        "is_active": True,
    },
])


# ============================================================
# 11. HEALTHCARE & LIFE SCIENCES
# ============================================================

CANONICAL_ROLES.extend([

    # --------------------------------------------------------
    # 1. Clinical & Medical Practice
    # --------------------------------------------------------

    {
        "id": "general_practitioner",
        "name": "General Practitioner",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Provides primary medical care, diagnoses common illnesses and manages general patient health.",
        "is_active": True
    },
    {
        "id": "family_medicine_physician",
        "name": "Family Medicine Physician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Provides comprehensive primary healthcare across different ages and stages of life.",
        "is_active": True
    },
    {
        "id": "internal_medicine_physician",
        "name": "Internal Medicine Physician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Diagnoses and treats adult diseases, complex medical conditions and chronic illnesses.",
        "is_active": True
    },
    {
        "id": "specialist_physician",
        "name": "Specialist Physician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Provides specialist medical diagnosis and treatment within a defined clinical discipline.",
        "is_active": True
    },
    {
        "id": "consultant_physician",
        "name": "Consultant Physician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Provides senior specialist medical expertise, consultations and clinical treatment.",
        "is_active": True
    },
    {
        "id": "surgeon",
        "name": "Surgeon",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Performs surgical procedures to treat injuries, diseases and medical conditions.",
        "is_active": True
    },
    {
        "id": "general_surgeon",
        "name": "General Surgeon",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Performs surgical procedures involving abdominal organs, soft tissues and general surgical conditions.",
        "is_active": True
    },
    {
        "id": "emergency_medicine_physician",
        "name": "Emergency Medicine Physician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Diagnoses and treats urgent, life-threatening and emergency medical conditions.",
        "is_active": True
    },
    {
        "id": "pediatrician",
        "name": "Pediatrician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Provides medical care, diagnosis and treatment for infants, children and adolescents.",
        "is_active": True
    },
    {
        "id": "cardiologist",
        "name": "Cardiologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Diagnoses and treats diseases and disorders of the heart and cardiovascular system.",
        "is_active": True
    },
    {
        "id": "neurologist",
        "name": "Neurologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Diagnoses and treats disorders affecting the brain, spinal cord and nervous system.",
        "is_active": True
    },
    {
        "id": "anesthesiologist",
        "name": "Anesthesiologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Provides anesthesia, pain management and perioperative medical care.",
        "is_active": True
    },
    {
        "id": "dermatologist",
        "name": "Dermatologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_medical_practice",
        "description": "Diagnoses and treats diseases and conditions affecting skin, hair and nails.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 2. Nursing & Patient Care
    # --------------------------------------------------------

    {
        "id": "registered_nurse",
        "name": "Registered Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides professional nursing care, monitors patients and coordinates clinical treatment.",
        "is_active": True
    },
    {
        "id": "staff_nurse",
        "name": "Staff Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Delivers routine and specialised nursing care in hospitals and healthcare facilities.",
        "is_active": True
    },
    {
        "id": "nurse_practitioner",
        "name": "Nurse Practitioner",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides advanced nursing assessment, diagnosis and patient treatment within authorised scope.",
        "is_active": True
    },
    {
        "id": "clinical_nurse_specialist",
        "name": "Clinical Nurse Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides advanced clinical nursing expertise in a specialised patient-care area.",
        "is_active": True
    },
    {
        "id": "nurse_manager",
        "name": "Nurse Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Manages nursing teams, staffing, patient-care standards and nursing department operations.",
        "is_active": True
    },
    {
        "id": "nursing_supervisor",
        "name": "Nursing Supervisor",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Supervises nursing staff, clinical workflows and day-to-day nursing service delivery.",
        "is_active": True
    },
    {
        "id": "critical_care_nurse",
        "name": "Critical Care Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides specialised nursing care to critically ill patients in intensive care settings.",
        "is_active": True
    },
    {
        "id": "emergency_nurse",
        "name": "Emergency Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides immediate nursing assessment and treatment for patients in emergency departments.",
        "is_active": True
    },
    {
        "id": "operating_room_nurse",
        "name": "Operating Room Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Supports surgical procedures and provides nursing care before, during and after surgery.",
        "is_active": True
    },
    {
        "id": "pediatric_nurse",
        "name": "Pediatric Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides specialised nursing care to infants, children and adolescents.",
        "is_active": True
    },
    {
        "id": "oncology_nurse",
        "name": "Oncology Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides nursing care, treatment support and patient education for people with cancer.",
        "is_active": True
    },
    {
        "id": "community_health_nurse",
        "name": "Community Health Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Delivers community-based nursing services, preventive care and public health education.",
        "is_active": True
    },
    {
        "id": "home_health_nurse",
        "name": "Home Health Nurse",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "nursing_patient_care",
        "description": "Provides nursing assessments, treatment and ongoing patient care in home settings.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 3. Pharmacy & Pharmaceutical Sciences
    # --------------------------------------------------------

    {
        "id": "pharmacist",
        "name": "Pharmacist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Dispenses medications and advises patients and healthcare professionals on their safe use.",
        "is_active": True
    },
    {
        "id": "clinical_pharmacist",
        "name": "Clinical Pharmacist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Reviews medication therapy and supports safe and effective clinical medication management.",
        "is_active": True
    },
    {
        "id": "hospital_pharmacist",
        "name": "Hospital Pharmacist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Manages medication dispensing, inventory and pharmaceutical services within hospitals.",
        "is_active": True
    },
    {
        "id": "community_pharmacist",
        "name": "Community Pharmacist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Dispenses prescriptions and provides medication advice and healthcare guidance in community pharmacies.",
        "is_active": True
    },
    {
        "id": "pharmaceutical_scientist",
        "name": "Pharmaceutical Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Conducts scientific research and development involving pharmaceutical products and medicines.",
        "is_active": True
    },
    {
        "id": "formulation_scientist",
        "name": "Formulation Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Develops and optimises pharmaceutical formulations, dosage forms and drug delivery systems.",
        "is_active": True
    },
    {
        "id": "pharmaceutical_research_scientist",
        "name": "Pharmaceutical Research Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Conducts laboratory and applied research supporting pharmaceutical discovery and development.",
        "is_active": True
    },
    {
        "id": "pharmacovigilance_specialist",
        "name": "Pharmacovigilance Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Monitors, assesses and reports adverse drug reactions and medication safety information.",
        "is_active": True
    },
    {
        "id": "pharmaceutical_quality_control_analyst",
        "name": "Pharmaceutical Quality Control Analyst",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Tests pharmaceutical raw materials and finished products against quality specifications.",
        "is_active": True
    },
    {
        "id": "pharmaceutical_manufacturing_specialist",
        "name": "Pharmaceutical Manufacturing Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Supports manufacturing processes and production of pharmaceutical products.",
        "is_active": True
    },
    {
        "id": "pharmaceutical_validation_specialist",
        "name": "Pharmaceutical Validation Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Validates pharmaceutical manufacturing processes, equipment and systems for compliance.",
        "is_active": True
    },
    {
        "id": "drug_safety_associate",
        "name": "Drug Safety Associate",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Processes and evaluates drug safety reports and supports pharmacovigilance operations.",
        "is_active": True
    },
    {
        "id": "pharmacy_manager",
        "name": "Pharmacy Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "pharmacy_pharmaceutical_sciences",
        "description": "Manages pharmacy operations, staff, medication inventory and dispensing services.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 4. Allied Health & Rehabilitation
    # --------------------------------------------------------

    {
        "id": "physiotherapist",
        "name": "Physiotherapist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Assesses and treats physical movement, mobility and functional rehabilitation needs.",
        "is_active": True
    },
    {
        "id": "occupational_therapist",
        "name": "Occupational Therapist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Helps patients improve independence and daily living skills through therapeutic interventions.",
        "is_active": True
    },
    {
        "id": "speech_language_pathologist",
        "name": "Speech-Language Pathologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Assesses and treats speech, language, communication and swallowing disorders.",
        "is_active": True
    },
    {
        "id": "audiologist",
        "name": "Audiologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Evaluates hearing and balance disorders and provides related diagnostic and rehabilitative services.",
        "is_active": True
    },
    {
        "id": "radiographer",
        "name": "Radiographer",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Performs diagnostic medical imaging procedures using radiographic equipment.",
        "is_active": True
    },
    {
        "id": "medical_imaging_technologist",
        "name": "Medical Imaging Technologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Operates medical imaging systems and supports diagnostic imaging examinations.",
        "is_active": True
    },
    {
        "id": "sonographer",
        "name": "Sonographer",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Performs diagnostic ultrasound examinations and produces clinical imaging information.",
        "is_active": True
    },
    {
        "id": "dietitian",
        "name": "Dietitian",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Assesses nutritional needs and develops evidence-based dietary and therapeutic nutrition plans.",
        "is_active": True
    },
    {
        "id": "respiratory_therapist",
        "name": "Respiratory Therapist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Assesses and treats patients with breathing and cardiopulmonary disorders.",
        "is_active": True
    },
    {
        "id": "prosthetist_orthotist",
        "name": "Prosthetist and Orthotist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Designs and fits prosthetic and orthotic devices to support mobility and physical function.",
        "is_active": True
    },
    {
        "id": "optometrist",
        "name": "Optometrist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Examines vision, identifies visual disorders and provides primary eye-care services.",
        "is_active": True
    },
    {
        "id": "paramedic",
        "name": "Paramedic",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Provides emergency medical assessment, stabilisation and pre-hospital patient care.",
        "is_active": True
    },
    {
        "id": "emergency_medical_technician",
        "name": "Emergency Medical Technician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "allied_health_rehabilitation",
        "description": "Provides emergency medical assistance and basic pre-hospital patient care.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 5. Medical Laboratory & Diagnostics
    # --------------------------------------------------------

    {
        "id": "medical_lab_technologist",
        "name": "Medical Laboratory Technologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Performs clinical laboratory testing and diagnostic procedures on patient specimens.",
        "is_active": True
    },
    {
        "id": "medical_lab_scientist",
        "name": "Medical Laboratory Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Conducts complex laboratory analyses supporting disease diagnosis and clinical decisions.",
        "is_active": True
    },
    {
        "id": "clinical_lab_technician",
        "name": "Clinical Laboratory Technician",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Collects, prepares and analyses clinical specimens using laboratory equipment and methods.",
        "is_active": True
    },
    {
        "id": "laboratory_manager",
        "name": "Laboratory Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Manages laboratory staff, equipment, workflows, quality systems and testing operations.",
        "is_active": True
    },
    {
        "id": "histotechnologist",
        "name": "Histotechnologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Prepares and processes tissue specimens for microscopic examination and diagnosis.",
        "is_active": True
    },
    {
        "id": "cytotechnologist",
        "name": "Cytotechnologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Examines cellular specimens to identify abnormalities and support disease diagnosis.",
        "is_active": True
    },
    {
        "id": "clinical_microbiologist",
        "name": "Clinical Microbiologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Studies clinical microorganisms and performs diagnostic testing for infectious diseases.",
        "is_active": True
    },
    {
        "id": "medical_lab_quality_specialist",
        "name": "Medical Laboratory Quality Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Maintains laboratory quality assurance, accreditation and diagnostic testing standards.",
        "is_active": True
    },
    {
        "id": "clinical_pathologist",
        "name": "Clinical Pathologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Interprets laboratory investigations and supports diagnosis through clinical pathology.",
        "is_active": True
    },
    {
        "id": "phlebotomist",
        "name": "Phlebotomist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Collects blood samples from patients for laboratory testing and clinical investigations.",
        "is_active": True
    },
    {
        "id": "blood_bank_technologist",
        "name": "Blood Bank Technologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Performs blood grouping, compatibility testing and blood bank laboratory procedures.",
        "is_active": True
    },
    {
        "id": "molecular_diagnostics_technologist",
        "name": "Molecular Diagnostics Technologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Performs molecular diagnostic testing using techniques such as PCR and nucleic acid analysis.",
        "is_active": True
    },
    {
        "id": "clinical_chemistry_technologist",
        "name": "Clinical Chemistry Technologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "medical_laboratory_diagnostics",
        "description": "Performs biochemical and clinical chemistry tests to support disease diagnosis.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 6. Public Health & Healthcare Administration
    # --------------------------------------------------------

    {
        "id": "public_health_specialist",
        "name": "Public Health Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Develops and supports public health programmes, prevention strategies and population health initiatives.",
        "is_active": True
    },
    {
        "id": "epidemiologist",
        "name": "Epidemiologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Studies disease patterns, risk factors and population health trends to guide interventions.",
        "is_active": True
    },
    {
        "id": "public_health_officer",
        "name": "Public Health Officer",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Implements public health programmes, monitoring activities and community health initiatives.",
        "is_active": True
    },
    {
        "id": "healthcare_administrator",
        "name": "Healthcare Administrator",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Coordinates administrative functions, resources and services within healthcare organisations.",
        "is_active": True
    },
    {
        "id": "hospital_administrator",
        "name": "Hospital Administrator",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Oversees hospital administration, staffing, resources and institutional operations.",
        "is_active": True
    },
    {
        "id": "healthcare_operations_manager",
        "name": "Healthcare Operations Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Manages healthcare service delivery, operational performance and process efficiency.",
        "is_active": True
    },
    {
        "id": "health_information_manager",
        "name": "Health Information Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Manages healthcare information systems, medical data governance and health records.",
        "is_active": True
    },
    {
        "id": "healthcare_quality_manager",
        "name": "Healthcare Quality Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Leads healthcare quality improvement, patient safety and clinical service standards.",
        "is_active": True
    },
    {
        "id": "medical_records_officer",
        "name": "Medical Records Officer",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Maintains patient medical records, documentation accuracy and records administration.",
        "is_active": True
    },
    {
        "id": "health_services_manager",
        "name": "Health Services Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Plans and manages healthcare services, clinical support functions and service delivery.",
        "is_active": True
    },
    {
        "id": "infection_preventionist",
        "name": "Infection Preventionist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Develops and monitors infection prevention and control programmes in healthcare settings.",
        "is_active": True
    },
    {
        "id": "health_economist",
        "name": "Health Economist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Analyses healthcare costs, resource allocation and economic outcomes of health interventions.",
        "is_active": True
    },
    {
        "id": "community_health_worker",
        "name": "Community Health Worker",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "public_healthcare_administration",
        "description": "Connects communities with healthcare services and supports health education and outreach.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 7. Biotechnology & Biomedical Research
    # --------------------------------------------------------

    {
        "id": "biotechnologist",
        "name": "Biotechnologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Applies biological sciences and technology to develop products and processes.",
        "is_active": True
    },
    {
        "id": "biomedical_scientist",
        "name": "Biomedical Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Applies biomedical science to investigate human health, disease and biological processes.",
        "is_active": True
    },
    {
        "id": "biomedical_research_scientist",
        "name": "Biomedical Research Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Conducts research into biological mechanisms, diseases and potential medical treatments.",
        "is_active": True
    },
    {
        "id": "molecular_biologist",
        "name": "Molecular Biologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Studies molecular mechanisms and interactions involving DNA, RNA, proteins and cells.",
        "is_active": True
    },
    {
        "id": "geneticist",
        "name": "Geneticist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Studies genes, inheritance and genetic variation in biological systems and diseases.",
        "is_active": True
    },
    {
        "id": "bioinformatics_scientist",
        "name": "Bioinformatics Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Uses computational methods to analyse biological, genomic and molecular datasets.",
        "is_active": True
    },
    {
        "id": "cell_culture_scientist",
        "name": "Cell Culture Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Develops and maintains cell culture systems for research and biotechnology applications.",
        "is_active": True
    },
    {
        "id": "bioprocess_scientist",
        "name": "Bioprocess Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Develops and optimises biological production processes and biomanufacturing systems.",
        "is_active": True
    },
    {
        "id": "microbiologist",
        "name": "Microbiologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Studies microorganisms and their applications in healthcare, research and biotechnology.",
        "is_active": True
    },
    {
        "id": "immunologist",
        "name": "Immunologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Studies immune system functions, immune disorders and immune-based treatments.",
        "is_active": True
    },
    {
        "id": "virologist",
        "name": "Virologist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Studies viruses, viral diseases and methods for detection, prevention and treatment.",
        "is_active": True
    },
    {
        "id": "protein_scientist",
        "name": "Protein Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Studies protein structure, function and interactions for biomedical and biotechnology applications.",
        "is_active": True
    },
    {
        "id": "genomics_scientist",
        "name": "Genomics Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "biotechnology_biomedical_research",
        "description": "Analyses genomes and genetic variation to support biological and biomedical research.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 8. Clinical Research & Regulatory Affairs
    # --------------------------------------------------------

    {
        "id": "clinical_research_associate",
        "name": "Clinical Research Associate",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Monitors clinical trials and verifies compliance with study protocols and research standards.",
        "is_active": True
    },
    {
        "id": "clinical_research_coordinator",
        "name": "Clinical Research Coordinator",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Coordinates clinical study activities, participant enrolment and research documentation.",
        "is_active": True
    },
    {
        "id": "clinical_research_manager",
        "name": "Clinical Research Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Manages clinical research programmes, study teams, timelines and research compliance.",
        "is_active": True
    },
    {
        "id": "clinical_trial_manager",
        "name": "Clinical Trial Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Oversees clinical trial execution, site activities, milestones and trial performance.",
        "is_active": True
    },
    {
        "id": "clinical_data_manager",
        "name": "Clinical Data Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Manages clinical trial data collection, validation, quality and database processes.",
        "is_active": True
    },
    {
        "id": "regulatory_affairs_specialist",
        "name": "Regulatory Affairs Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Supports regulatory submissions, product registrations and compliance with health regulations.",
        "is_active": True
    },
    {
        "id": "regulatory_affairs_manager",
        "name": "Regulatory Affairs Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Leads regulatory strategy, submissions and compliance for healthcare and life-sciences products.",
        "is_active": True
    },
    {
        "id": "clinical_research_scientist",
        "name": "Clinical Research Scientist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Designs and conducts clinical research to evaluate medical treatments and interventions.",
        "is_active": True
    },
    {
        "id": "clinical_operations_manager",
        "name": "Clinical Operations Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Manages clinical research operations, study delivery and clinical team coordination.",
        "is_active": True
    },
    {
        "id": "clinical_trial_assistant",
        "name": "Clinical Trial Assistant",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Provides administrative and documentation support for clinical trial activities.",
        "is_active": True
    },
    {
        "id": "clinical_quality_assurance_specialist",
        "name": "Clinical Quality Assurance Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Audits clinical research processes and ensures compliance with quality standards and protocols.",
        "is_active": True
    },
    {
        "id": "regulatory_submissions_specialist",
        "name": "Regulatory Submissions Specialist",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Prepares, coordinates and maintains regulatory submissions and supporting documentation.",
        "is_active": True
    },
    {
        "id": "clinical_project_manager",
        "name": "Clinical Project Manager",
        "professional_field_id": "healthcare_life_sciences",
        "subfield_id": "clinical_research_regulatory_affairs",
        "description": "Plans and delivers clinical research projects, managing resources, milestones and stakeholders.",
        "is_active": True
    },

])

# ============================================================
# 12. OTHER PROFESSIONAL ROLES
# ============================================================

CANONICAL_ROLES.extend([

    # --------------------------------------------------------
    # 1. Government & Public Administration
    # --------------------------------------------------------

    {
        "id": "public_administration_officer",
        "name": "Public Administration Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Coordinates government administration, public services and administrative programmes.",
        "is_active": True
    },
    {
        "id": "government_relations_officer",
        "name": "Government Relations Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Manages relationships and communications between organisations and government authorities.",
        "is_active": True
    },
    {
        "id": "civil_service_officer",
        "name": "Civil Service Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Performs public administration and government policy implementation responsibilities within civil services.",
        "is_active": True
    },
    {
        "id": "policy_analyst",
        "name": "Policy Analyst",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Analyses public policies, evaluates their impact and develops evidence-based recommendations.",
        "is_active": True
    },
    {
        "id": "public_policy_officer",
        "name": "Public Policy Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Develops, coordinates and implements public policy initiatives and government programmes.",
        "is_active": True
    },
    {
        "id": "public_administration_manager",
        "name": "Public Administration Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Manages public sector administrative functions, teams, resources and service delivery.",
        "is_active": True
    },
    {
        "id": "government_program_officer",
        "name": "Government Program Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Coordinates government programmes, implementation activities and public sector projects.",
        "is_active": True
    },
    {
        "id": "municipal_administrator",
        "name": "Municipal Administrator",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Oversees municipal administration, local government services and civic operations.",
        "is_active": True
    },
    {
        "id": "urban_government_planner",
        "name": "Urban Government Planner",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Supports public sector urban planning, municipal development and land-use policy.",
        "is_active": True
    },
    {
        "id": "legislative_affairs_specialist",
        "name": "Legislative Affairs Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Monitors legislation, prepares policy briefs and coordinates legislative engagement.",
        "is_active": True
    },
    {
        "id": "public_sector_consultant",
        "name": "Public Sector Consultant",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Advises government organisations on policy, administration and public service improvement.",
        "is_active": True
    },
    {
        "id": "diplomatic_officer",
        "name": "Diplomatic Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Represents national interests and supports diplomatic relations and international affairs.",
        "is_active": True
    },
    {
        "id": "foreign_service_officer",
        "name": "Foreign Service Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Conducts diplomatic, consular and international government service activities.",
        "is_active": True
    },
    {
        "id": "election_administration_officer",
        "name": "Election Administration Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "government_public_administration",
        "description": "Coordinates election administration, voter services and electoral compliance activities.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 2. Policy, International Development & NGOs
    # --------------------------------------------------------

    {
        "id": "ngo_program_officer",
        "name": "NGO Program Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Coordinates nonprofit programmes, project activities and community development initiatives.",
        "is_active": True
    },
    {
        "id": "ngo_program_manager",
        "name": "NGO Program Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Manages NGO programmes, project teams, budgets and programme outcomes.",
        "is_active": True
    },
    {
        "id": "international_development_specialist",
        "name": "International Development Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Designs and supports international development initiatives and socioeconomic programmes.",
        "is_active": True
    },
    {
        "id": "humanitarian_affairs_officer",
        "name": "Humanitarian Affairs Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Supports humanitarian response, relief coordination and emergency assistance programmes.",
        "is_active": True
    },
    {
        "id": "humanitarian_project_manager",
        "name": "Humanitarian Project Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Manages humanitarian projects, emergency response activities and relief operations.",
        "is_active": True
    },
    {
        "id": "grants_manager",
        "name": "Grants Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Manages grant applications, funding agreements, budgets and grant compliance.",
        "is_active": True
    },
    {
        "id": "ngo_partnerships_manager",
        "name": "NGO Partnerships Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Develops and manages partnerships between NGOs, donors and development organisations.",
        "is_active": True
    },
    {
        "id": "nonprofit_fundraising_manager",
        "name": "Nonprofit Fundraising Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Leads fundraising strategies, donor engagement and charitable funding initiatives.",
        "is_active": True
    },
    {
        "id": "monitoring_evaluation_learning_specialist",
        "name": "Monitoring, Evaluation and Learning Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Designs monitoring and evaluation frameworks and measures development programme outcomes.",
        "is_active": True
    },
    {
        "id": "community_development_officer",
        "name": "Community Development Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Coordinates community development projects, local engagement and social improvement initiatives.",
        "is_active": True
    },
    {
        "id": "livelihoods_officer",
        "name": "Livelihoods Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Develops livelihood programmes supporting employment, income generation and economic resilience.",
        "is_active": True
    },
    {
        "id": "social_impact_manager",
        "name": "Social Impact Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Manages social impact initiatives and evaluates organisational contributions to communities.",
        "is_active": True
    },
    {
        "id": "advocacy_campaigns_manager",
        "name": "Advocacy and Campaigns Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Leads advocacy strategies, public campaigns and stakeholder engagement initiatives.",
        "is_active": True
    },
    {
        "id": "humanitarian_logistics_coordinator",
        "name": "Humanitarian Logistics Coordinator",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "policy_international_development_ngos",
        "description": "Coordinates supply distribution, transportation and logistics for humanitarian operations.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 3. Research, Think Tanks & Social Sciences
    # --------------------------------------------------------

    {
        "id": "social_researcher",
        "name": "Social Researcher",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Conducts research into social behaviour, communities and societal trends.",
        "is_active": True
    },
    {
        "id": "social_scientist",
        "name": "Social Scientist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Studies human societies, institutions and social relationships using scientific methods.",
        "is_active": True
    },
    {
        "id": "sociologist",
        "name": "Sociologist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Researches social structures, institutions, relationships and patterns of human behaviour.",
        "is_active": True
    },
    {
        "id": "political_scientist",
        "name": "Political Scientist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Studies political systems, institutions, governance and political behaviour.",
        "is_active": True
    },
    {
        "id": "demographer",
        "name": "Demographer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Analyses population characteristics, demographic changes and population trends.",
        "is_active": True
    },
    {
        "id": "anthropologist",
        "name": "Anthropologist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Studies human cultures, societies, social practices and human development.",
        "is_active": True
    },
    {
        "id": "research_fellow",
        "name": "Research Fellow",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Conducts independent or collaborative research within academic and research institutions.",
        "is_active": True
    },
    {
        "id": "think_tank_researcher",
        "name": "Think Tank Researcher",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Conducts policy-oriented research and develops evidence-based recommendations for public issues.",
        "is_active": True
    },
    {
        "id": "public_policy_researcher",
        "name": "Public Policy Researcher",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Researches public policy challenges, government programmes and policy outcomes.",
        "is_active": True
    },
    {
        "id": "qualitative_researcher",
        "name": "Qualitative Researcher",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Conducts qualitative studies using interviews, observations and thematic research methods.",
        "is_active": True
    },
    {
        "id": "survey_researcher",
        "name": "Survey Researcher",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Designs and conducts surveys and analyses responses for research purposes.",
        "is_active": True
    },
    {
        "id": "evaluation_researcher",
        "name": "Evaluation Researcher",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Evaluates programme effectiveness, research interventions and organisational outcomes.",
        "is_active": True
    },
    {
        "id": "research_program_manager",
        "name": "Research Program Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Manages research programmes, project resources, timelines and research teams.",
        "is_active": True
    },
    {
        "id": "research_director",
        "name": "Research Director",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "research_think_tanks_social_sciences",
        "description": "Leads research strategy, research teams and institutional research programmes.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 4. Environment & Sustainability
    # --------------------------------------------------------

    {
        "id": "environmental_scientist",
        "name": "Environmental Scientist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Studies environmental conditions, pollution and ecological impacts through scientific research.",
        "is_active": True
    },
    {
        "id": "environmental_consultant",
        "name": "Environmental Consultant",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Advises organisations on environmental management, assessments and regulatory compliance.",
        "is_active": True
    },
    {
        "id": "sustainability_specialist",
        "name": "Sustainability Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Supports sustainability programmes, environmental initiatives and responsible business practices.",
        "is_active": True
    },
    {
        "id": "sustainability_manager",
        "name": "Sustainability Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Leads organisational sustainability strategy, performance measurement and environmental programmes.",
        "is_active": True
    },
    {
        "id": "climate_change_analyst",
        "name": "Climate Change Analyst",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Analyses climate trends, climate risks and mitigation or adaptation strategies.",
        "is_active": True
    },
    {
        "id": "climate_policy_specialist",
        "name": "Climate Policy Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Develops and evaluates climate policies and environmental policy initiatives.",
        "is_active": True
    },
    {
        "id": "environmental_compliance_specialist",
        "name": "Environmental Compliance Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Ensures compliance with environmental regulations, permits and operational standards.",
        "is_active": True
    },
    {
        "id": "environmental_impact_assessment_specialist",
        "name": "Environmental Impact Assessment Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Conducts environmental impact assessments for infrastructure and development projects.",
        "is_active": True
    },
    {
        "id": "conservation_officer",
        "name": "Conservation Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Supports biodiversity conservation, habitat protection and natural resource management.",
        "is_active": True
    },
    {
        "id": "biodiversity_specialist",
        "name": "Biodiversity Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Studies and supports the conservation of biodiversity, ecosystems and species.",
        "is_active": True
    },
    {
        "id": "waste_management_specialist",
        "name": "Waste Management Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Develops waste management, recycling and resource recovery programmes.",
        "is_active": True
    },
    {
        "id": "renewable_energy_policy_specialist",
        "name": "Renewable Energy Policy Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Supports policy development and analysis for renewable energy adoption and regulation.",
        "is_active": True
    },
    {
        "id": "carbon_accounting_specialist",
        "name": "Carbon Accounting Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Measures and reports greenhouse gas emissions and organisational carbon footprints.",
        "is_active": True
    },
    {
        "id": "environmental_program_manager",
        "name": "Environmental Program Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "environment_sustainability",
        "description": "Manages environmental programmes, conservation projects and sustainability initiatives.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 5. Agriculture & Agribusiness
    # --------------------------------------------------------

    {
        "id": "agronomist",
        "name": "Agronomist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Advises on crop production, soil management and agricultural productivity.",
        "is_active": True
    },
    {
        "id": "agricultural_scientist",
        "name": "Agricultural Scientist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Conducts scientific research to improve agricultural production and farming systems.",
        "is_active": True
    },
    {
        "id": "agricultural_extension_officer",
        "name": "Agricultural Extension Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Provides farmers with agricultural advice, training and information about improved farming practices.",
        "is_active": True
    },
    {
        "id": "farm_manager",
        "name": "Farm Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Oversees farm operations, production activities, workers and agricultural resources.",
        "is_active": True
    },
    {
        "id": "agricultural_manager",
        "name": "Agricultural Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Manages agricultural production, operations and business activities.",
        "is_active": True
    },
    {
        "id": "agribusiness_manager",
        "name": "Agribusiness Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Manages commercial operations, strategy and business development within agricultural enterprises.",
        "is_active": True
    },
    {
        "id": "agricultural_economist",
        "name": "Agricultural Economist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Analyses agricultural markets, farm economics, commodity pricing and rural development.",
        "is_active": True
    },
    {
        "id": "horticulturist",
        "name": "Horticulturist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Studies and manages the cultivation of fruits, vegetables, ornamental plants and crops.",
        "is_active": True
    },
    {
        "id": "soil_scientist",
        "name": "Soil Scientist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Studies soil composition, fertility and properties to support agriculture and land management.",
        "is_active": True
    },
    {
        "id": "crop_protection_specialist",
        "name": "Crop Protection Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Develops and implements strategies to protect crops against pests, diseases and weeds.",
        "is_active": True
    },
    {
        "id": "livestock_manager",
        "name": "Livestock Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Manages livestock production, animal husbandry and farm animal operations.",
        "is_active": True
    },
    {
        "id": "animal_scientist",
        "name": "Animal Scientist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Studies animal biology, nutrition, breeding and livestock production systems.",
        "is_active": True
    },
    {
        "id": "irrigation_specialist",
        "name": "Irrigation Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Plans and manages irrigation systems and agricultural water-use efficiency.",
        "is_active": True
    },
    {
        "id": "agricultural_inspector",
        "name": "Agricultural Inspector",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "agriculture_agribusiness",
        "description": "Inspects agricultural products, farming operations and compliance with agricultural standards.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 6. Real Estate & Property Management
    # --------------------------------------------------------

    {
        "id": "real_estate_agent",
        "name": "Real Estate Agent",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Assists clients with buying, selling and renting residential or commercial properties.",
        "is_active": True
    },
    {
        "id": "real_estate_broker",
        "name": "Real Estate Broker",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Oversees property transactions, brokerage operations and real estate client relationships.",
        "is_active": True
    },
    {
        "id": "property_manager",
        "name": "Property Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Manages property operations, tenants, maintenance and property-related services.",
        "is_active": True
    },
    {
        "id": "property_administrator",
        "name": "Property Administrator",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Coordinates property documentation, tenant records and administrative property services.",
        "is_active": True
    },
    {
        "id": "leasing_manager",
        "name": "Leasing Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Manages leasing operations, rental agreements and occupancy performance.",
        "is_active": True
    },
    {
        "id": "leasing_consultant",
        "name": "Leasing Consultant",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Markets available properties and assists prospective tenants with leasing arrangements.",
        "is_active": True
    },
    {
        "id": "real_estate_analyst",
        "name": "Real Estate Analyst",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Analyses property markets, investment opportunities and real estate financial performance.",
        "is_active": True
    },
    {
        "id": "real_estate_development_manager",
        "name": "Real Estate Development Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Manages property development projects, feasibility studies and development activities.",
        "is_active": True
    },
    {
        "id": "real_estate_valuation_surveyor",
        "name": "Real Estate Valuation Surveyor",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Assesses property values and prepares professional real estate valuation reports.",
        "is_active": True
    },
    {
        "id": "property_appraiser",
        "name": "Property Appraiser",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Evaluates property values using market evidence and professional appraisal methods.",
        "is_active": True
    },
    {
        "id": "property_asset_manager",
        "name": "Property Asset Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Manages the financial and operational performance of property assets and portfolios.",
        "is_active": True
    },
    {
        "id": "real_estate_transaction_coordinator",
        "name": "Real Estate Transaction Coordinator",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Coordinates real estate transaction documentation, deadlines and stakeholder communications.",
        "is_active": True
    },
    {
        "id": "property_acquisition_manager",
        "name": "Property Acquisition Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Identifies and manages property acquisition opportunities and investment transactions.",
        "is_active": True
    },
    {
        "id": "real_estate_portfolio_manager",
        "name": "Real Estate Portfolio Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "real_estate_property_management",
        "description": "Oversees real estate investment portfolios, asset allocation and portfolio performance.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 7. Security, Defence & Public Safety
    # --------------------------------------------------------

    {
        "id": "security_officer",
        "name": "Security Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Maintains physical security, monitors premises and supports safety procedures.",
        "is_active": True
    },
    {
        "id": "security_manager",
        "name": "Security Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Manages physical security programmes, security personnel and organisational protection measures.",
        "is_active": True
    },
    {
        "id": "security_operations_manager",
        "name": "Security Operations Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Oversees security operations, personnel deployment and operational security procedures.",
        "is_active": True
    },
    {
        "id": "security_supervisor",
        "name": "Security Supervisor",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Supervises security teams, site protection activities and security shift operations.",
        "is_active": True
    },
    {
        "id": "close_protection_officer",
        "name": "Close Protection Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Provides personal protection and security services for individuals requiring protective support.",
        "is_active": True
    },
    {
        "id": "corporate_security_manager",
        "name": "Corporate Security Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Manages corporate physical security, personnel protection and organisational security programmes.",
        "is_active": True
    },
    {
        "id": "loss_prevention_manager",
        "name": "Loss Prevention Manager",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Develops loss prevention strategies to reduce theft, fraud and operational losses.",
        "is_active": True
    },
    {
        "id": "defence_analyst",
        "name": "Defence Analyst",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Analyses defence policy, security developments and defence-related strategic information.",
        "is_active": True
    },
    {
        "id": "defence_program_officer",
        "name": "Defence Program Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Coordinates defence programmes, administrative activities and programme implementation.",
        "is_active": True
    },
    {
        "id": "military_operations_analyst",
        "name": "Military Operations Analyst",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Analyses military operations, operational planning and defence programme effectiveness.",
        "is_active": True
    },
    {
        "id": "emergency_management_specialist",
        "name": "Emergency Management Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Develops emergency preparedness, response and recovery plans for organisations and communities.",
        "is_active": True
    },
    {
        "id": "emergency_response_coordinator",
        "name": "Emergency Response Coordinator",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Coordinates emergency response teams, incident management and response activities.",
        "is_active": True
    },
    {
        "id": "disaster_risk_reduction_specialist",
        "name": "Disaster Risk Reduction Specialist",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Develops strategies to reduce disaster risks and strengthen community resilience.",
        "is_active": True
    },
    {
        "id": "fire_safety_officer",
        "name": "Fire Safety Officer",
        "professional_field_id": "other_professional_roles",
        "subfield_id": "security_defence_public_safety",
        "description": "Implements fire prevention, safety inspections and emergency fire response procedures.",
        "is_active": True
    },

])


# ============================================================
# 13. EDUCATION & TRAINING
# ============================================================

CANONICAL_ROLES.extend([

    # --------------------------------------------------------
    # 1. Teaching & Classroom Education
    # --------------------------------------------------------

    {
        "id": "primary_school_teacher",
        "name": "Primary School Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Teaches foundational subjects and develops academic and social skills among primary school students.",
        "is_active": True
    },
    {
        "id": "secondary_school_teacher",
        "name": "Secondary School Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Teaches academic subjects and supports the learning and development of secondary school students.",
        "is_active": True
    },
    {
        "id": "high_school_teacher",
        "name": "High School Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Delivers subject-specific instruction and prepares students for higher education and examinations.",
        "is_active": True
    },
    {
        "id": "preschool_teacher",
        "name": "Preschool Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Provides early learning activities that support children's cognitive, social and emotional development.",
        "is_active": True
    },
    {
        "id": "early_childhood_educator",
        "name": "Early Childhood Educator",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Supports early childhood learning through age-appropriate educational activities and development programmes.",
        "is_active": True
    },
    {
        "id": "special_education_teacher",
        "name": "Special Education Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Provides specialised instruction and learning support for students with diverse educational needs.",
        "is_active": True
    },
    {
        "id": "substitute_teacher",
        "name": "Substitute Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Provides temporary classroom instruction and maintains continuity of teaching during staff absences.",
        "is_active": True
    },
    {
        "id": "classroom_teacher",
        "name": "Classroom Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Plans and delivers classroom lessons, assesses student progress and manages learning activities.",
        "is_active": True
    },
    {
        "id": "subject_teacher",
        "name": "Subject Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Provides specialised instruction in a particular academic subject across school grade levels.",
        "is_active": True
    },
    {
        "id": "mathematics_teacher",
        "name": "Mathematics Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Teaches mathematics concepts, problem-solving methods and quantitative reasoning skills.",
        "is_active": True
    },
    {
        "id": "science_teacher",
        "name": "Science Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Teaches scientific concepts and practical science through classroom instruction and experiments.",
        "is_active": True
    },
    {
        "id": "language_teacher",
        "name": "Language Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Teaches language skills including reading, writing, speaking and comprehension.",
        "is_active": True
    },
    {
        "id": "physical_education_teacher",
        "name": "Physical Education Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Teaches physical education, sports skills, fitness and healthy physical activity.",
        "is_active": True
    },
    {
        "id": "teaching_assistant",
        "name": "Teaching Assistant",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Supports teachers with classroom activities, student supervision and individual learning assistance.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 2. Higher Education & University Administration
    # --------------------------------------------------------

    {
        "id": "university_professor",
        "name": "University Professor",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Teaches university-level courses, conducts academic research and contributes to institutional scholarship.",
        "is_active": True
    },
    {
        "id": "assistant_professor",
        "name": "Assistant Professor",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Teaches undergraduate or postgraduate courses and develops an academic research portfolio.",
        "is_active": True
    },
    {
        "id": "associate_professor",
        "name": "Associate Professor",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Provides advanced university instruction, leads research activities and supports academic development.",
        "is_active": True
    },
    {
        "id": "lecturer",
        "name": "Lecturer",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Delivers lectures, prepares teaching materials and assesses students in higher education institutions.",
        "is_active": True
    },
    {
        "id": "senior_lecturer",
        "name": "Senior Lecturer",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Provides advanced academic instruction and contributes to curriculum and departmental development.",
        "is_active": True
    },
    {
        "id": "university_instructor",
        "name": "University Instructor",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Provides practical or theoretical instruction in university courses and academic programmes.",
        "is_active": True
    },
    {
        "id": "adjunct_faculty_member",
        "name": "Adjunct Faculty Member",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Provides part-time or contract-based teaching within colleges and universities.",
        "is_active": True
    },
    {
        "id": "university_admissions_officer",
        "name": "University Admissions Officer",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Coordinates student applications, admissions processes and enrolment activities.",
        "is_active": True
    },
    {
        "id": "academic_advisor",
        "name": "Academic Advisor",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Guides students on academic planning, course selection and educational progression.",
        "is_active": True
    },
    {
        "id": "university_registrar",
        "name": "University Registrar",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Oversees academic records, registration, institutional documentation and student administration.",
        "is_active": True
    },
    {
        "id": "university_administrator",
        "name": "University Administrator",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Coordinates administrative functions, academic services and university operations.",
        "is_active": True
    },
    {
        "id": "student_affairs_officer",
        "name": "Student Affairs Officer",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Coordinates student support services, extracurricular programmes and campus engagement.",
        "is_active": True
    },
    {
        "id": "university_department_coordinator",
        "name": "University Department Coordinator",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Coordinates departmental administration, academic schedules and faculty support activities.",
        "is_active": True
    },
    {
        "id": "academic_coordinator",
        "name": "Academic Coordinator",
        "professional_field_id": "education_training",
        "subfield_id": "higher_education_university_administration",
        "description": "Coordinates academic programmes, teaching schedules and curriculum implementation.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 3. Corporate Training & Learning Development
    # --------------------------------------------------------

    {
        "id": "corporate_trainer",
        "name": "Corporate Trainer",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Delivers employee training programmes to improve workplace knowledge and professional capabilities.",
        "is_active": True
    },
    {
        "id": "technical_trainer",
        "name": "Technical Trainer",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Provides technical training on software, systems, tools and specialised workplace technologies.",
        "is_active": True
    },
    {
        "id": "professional_skills_trainer",
        "name": "Professional Skills Trainer",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Trains employees in communication, leadership, teamwork and other professional workplace skills.",
        "is_active": True
    },
    {
        "id": "workplace_trainer",
        "name": "Workplace Trainer",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Delivers practical workplace training, onboarding and role-specific employee development.",
        "is_active": True
    },
    {
        "id": "training_facilitator",
        "name": "Training Facilitator",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Facilitates workshops, group learning sessions and interactive employee training activities.",
        "is_active": True
    },
    {
        "id": "leadership_development_trainer",
        "name": "Leadership Development Trainer",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Delivers leadership development programmes for managers and emerging organisational leaders.",
        "is_active": True
    },
    {
        "id": "employee_training_specialist",
        "name": "Employee Training Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Identifies employee training needs and develops programmes to improve workforce capabilities.",
        "is_active": True
    },
    {
        "id": "corporate_training_coordinator",
        "name": "Corporate Training Coordinator",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Coordinates corporate training schedules, learning sessions, resources and participant administration.",
        "is_active": True
    },
    {
        "id": "training_program_manager",
        "name": "Training Program Manager",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Manages employee training programmes, learning budgets, delivery plans and programme outcomes.",
        "is_active": True
    },
    {
        "id": "training_delivery_manager",
        "name": "Training Delivery Manager",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Oversees training delivery operations, instructors, learning schedules and programme quality.",
        "is_active": True
    },
    {
        "id": "learning_facilitator",
        "name": "Learning Facilitator",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Supports collaborative learning sessions, professional development and knowledge-sharing activities.",
        "is_active": True
    },
    {
        "id": "management_trainer",
        "name": "Management Trainer",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Trains managers in people management, business operations and organisational leadership practices.",
        "is_active": True
    },
    {
        "id": "customer_training_specialist",
        "name": "Customer Training Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Trains customers and clients to use products, platforms and business solutions effectively.",
        "is_active": True
    },
    {
        "id": "training_consultant",
        "name": "Training Consultant",
        "professional_field_id": "education_training",
        "subfield_id": "corporate_training_learning_development",
        "description": "Advises organisations on training strategies, learning needs and workforce development programmes.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 4. Instructional Design & E-Learning
    # --------------------------------------------------------

    {
        "id": "instructional_designer",
        "name": "Instructional Designer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Designs structured learning experiences, instructional materials and educational programmes.",
        "is_active": True
    },
    {
        "id": "senior_instructional_designer",
        "name": "Senior Instructional Designer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Leads instructional design projects and develops advanced learning strategies and educational content.",
        "is_active": True
    },
    {
        "id": "elearning_developer",
        "name": "E-Learning Developer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Develops digital learning courses, interactive training modules and online educational resources.",
        "is_active": True
    },
    {
        "id": "learning_experience_designer",
        "name": "Learning Experience Designer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Designs learner-centred educational experiences that improve engagement and learning outcomes.",
        "is_active": True
    },
    {
        "id": "curriculum_designer",
        "name": "Curriculum Designer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Designs curriculum structures, learning objectives and educational content frameworks.",
        "is_active": True
    },
    {
        "id": "curriculum_developer",
        "name": "Curriculum Developer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Develops and updates curricula, lesson plans and structured learning materials.",
        "is_active": True
    },
    {
        "id": "digital_learning_specialist",
        "name": "Digital Learning Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Develops and manages digital learning initiatives, online resources and technology-enabled education.",
        "is_active": True
    },
    {
        "id": "online_course_developer",
        "name": "Online Course Developer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Creates online courses, educational modules and digital instructional resources.",
        "is_active": True
    },
    {
        "id": "educational_content_developer",
        "name": "Educational Content Developer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Creates educational content, instructional resources and subject-specific learning materials.",
        "is_active": True
    },
    {
        "id": "learning_content_writer",
        "name": "Learning Content Writer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Writes structured educational content, course materials and instructional learning resources.",
        "is_active": True
    },
    {
        "id": "multimedia_learning_developer",
        "name": "Multimedia Learning Developer",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Creates multimedia learning materials using video, audio, graphics and interactive content.",
        "is_active": True
    },
    {
        "id": "learning_technology_specialist",
        "name": "Learning Technology Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Supports educational technology platforms and digital tools used in teaching and learning.",
        "is_active": True
    },
    {
        "id": "learning_management_system_administrator",
        "name": "Learning Management System Administrator",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Administers learning management systems, user access, course configurations and platform operations.",
        "is_active": True
    },
    {
        "id": "elearning_project_coordinator",
        "name": "E-Learning Project Coordinator",
        "professional_field_id": "education_training",
        "subfield_id": "instructional_design_elearning",
        "description": "Coordinates online learning development projects, delivery schedules and project resources.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 5. Academic Research & Educational Assessment
    # --------------------------------------------------------

    {
        "id": "education_researcher",
        "name": "Education Researcher",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Conducts research into teaching methods, educational systems and learning outcomes.",
        "is_active": True
    },
    {
        "id": "educational_research_analyst",
        "name": "Educational Research Analyst",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Analyses educational research data and prepares findings on institutional and student performance.",
        "is_active": True
    },
    {
        "id": "education_policy_researcher",
        "name": "Education Policy Researcher",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Researches education policies, regulatory developments and their effects on educational systems.",
        "is_active": True
    },
    {
        "id": "educational_assessment_specialist",
        "name": "Educational Assessment Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Develops and evaluates educational assessments, testing methods and student evaluation frameworks.",
        "is_active": True
    },
    {
        "id": "educational_measurement_specialist",
        "name": "Educational Measurement Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Applies measurement and statistical methods to assess educational achievement and learning performance.",
        "is_active": True
    },
    {
        "id": "assessment_coordinator",
        "name": "Assessment Coordinator",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Coordinates assessment schedules, examination processes and academic evaluation activities.",
        "is_active": True
    },
    {
        "id": "examination_officer",
        "name": "Examination Officer",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Coordinates examination administration, candidate records and assessment procedures.",
        "is_active": True
    },
    {
        "id": "examination_controller",
        "name": "Examination Controller",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Oversees examination administration, assessment integrity and examination governance.",
        "is_active": True
    },
    {
        "id": "academic_quality_assurance_specialist",
        "name": "Academic Quality Assurance Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Monitors academic standards and supports institutional quality assurance and accreditation processes.",
        "is_active": True
    },
    {
        "id": "institutional_research_analyst",
        "name": "Institutional Research Analyst",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Analyses institutional data to support academic planning, performance evaluation and decision-making.",
        "is_active": True
    },
    {
        "id": "education_evaluation_specialist",
        "name": "Education Evaluation Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Evaluates educational programmes, interventions and institutional effectiveness.",
        "is_active": True
    },
    {
        "id": "learning_outcomes_assessor",
        "name": "Learning Outcomes Assessor",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Assesses student learning outcomes against academic standards and programme objectives.",
        "is_active": True
    },
    {
        "id": "psychometric_assessment_specialist",
        "name": "Psychometric Assessment Specialist",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Develops and evaluates psychometric tests and measurement tools for educational assessment.",
        "is_active": True
    },
    {
        "id": "education_data_analyst",
        "name": "Education Data Analyst",
        "professional_field_id": "education_training",
        "subfield_id": "academic_research_educational_assessment",
        "description": "Analyses educational data to identify trends in enrolment, achievement and institutional performance.",
        "is_active": True
    },

    # --------------------------------------------------------
    # 6. Educational Leadership & Administration
    # --------------------------------------------------------

    {
        "id": "school_principal",
        "name": "School Principal",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Leads school operations, academic performance, staff management and institutional development.",
        "is_active": True
    },
    {
        "id": "vice_principal",
        "name": "Vice Principal",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Supports school leadership and oversees academic and administrative operations.",
        "is_active": True
    },
    {
        "id": "school_headmaster",
        "name": "School Headmaster",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Provides overall leadership and administrative direction for a school or educational institution.",
        "is_active": True
    },
    {
        "id": "school_administrator",
        "name": "School Administrator",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Manages school administration, records, scheduling and institutional support services.",
        "is_active": True
    },
    {
        "id": "school_director",
        "name": "School Director",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Leads school strategy, institutional operations and educational programme development.",
        "is_active": True
    },
    {
        "id": "academic_director",
        "name": "Academic Director",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Oversees academic strategy, curriculum standards and teaching quality across an institution.",
        "is_active": True
    },
    {
        "id": "education_program_director",
        "name": "Education Program Director",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Leads educational programmes, strategic initiatives and programme delivery across institutions.",
        "is_active": True
    },
    {
        "id": "education_manager",
        "name": "Education Manager",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Manages educational services, programme operations and institutional learning activities.",
        "is_active": True
    },
    {
        "id": "school_operations_manager",
        "name": "School Operations Manager",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Oversees school facilities, operational processes, support teams and administrative services.",
        "is_active": True
    },
    {
        "id": "education_coordinator",
        "name": "Education Coordinator",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Coordinates educational programmes, institutional activities and academic support operations.",
        "is_active": True
    },
    {
        "id": "district_education_officer",
        "name": "District Education Officer",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Oversees educational administration, school performance and education programmes across a district.",
        "is_active": True
    },
    {
        "id": "school_inspector",
        "name": "School Inspector",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Inspects schools and evaluates teaching standards, institutional compliance and educational quality.",
        "is_active": True
    },
    {
        "id": "education_superintendent",
        "name": "Education Superintendent",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Provides leadership and oversight for education systems, school networks and academic services.",
        "is_active": True
    },
    {
        "id": "education_administration_officer",
        "name": "Education Administration Officer",
        "professional_field_id": "education_training",
        "subfield_id": "educational_leadership_administration",
        "description": "Supports educational administration, institutional documentation and education service coordination.",
        "is_active": True
    },

])



# ============================================================
# LEGAL & COMPLIANCE — 84 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([

    # --------------------------------------------------------
    # 1. Legal Practice & Advisory
    # --------------------------------------------------------
    {
        "id": "lawyer",
        "name": "Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Provides legal advice, represents clients, and handles legal matters across applicable areas of law.",
        "is_active": True,
    },
    {
        "id": "legal_advisor",
        "name": "Legal Advisor",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Advises individuals and organizations on legal rights, obligations, and potential legal risks.",
        "is_active": True,
    },
    {
        "id": "legal_counsel",
        "name": "Legal Counsel",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Provides ongoing legal guidance and representation to clients or organizations.",
        "is_active": True,
    },
    {
        "id": "solicitor",
        "name": "Solicitor",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Advises clients, prepares legal documents, and manages legal matters in jurisdictions using the solicitor profession.",
        "is_active": True,
    },
    {
        "id": "barrister",
        "name": "Barrister",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Specializes in legal advocacy, court representation, and specialist legal opinions in relevant jurisdictions.",
        "is_active": True,
    },
    {
        "id": "litigation_lawyer",
        "name": "Litigation Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Handles disputes and represents clients in civil or commercial litigation proceedings.",
        "is_active": True,
    },
    {
        "id": "criminal_defense_lawyer",
        "name": "Criminal Defense Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Defends individuals and organizations facing criminal charges and related proceedings.",
        "is_active": True,
    },
    {
        "id": "civil_litigation_lawyer",
        "name": "Civil Litigation Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Represents clients in non-criminal disputes involving civil rights, obligations, and remedies.",
        "is_active": True,
    },
    {
        "id": "employment_lawyer",
        "name": "Employment Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Advises employers and employees on employment law, workplace disputes, and labor regulations.",
        "is_active": True,
    },
    {
        "id": "family_lawyer",
        "name": "Family Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Handles family-related legal matters including divorce, custody, adoption, and matrimonial disputes.",
        "is_active": True,
    },
    {
        "id": "legal_consultant",
        "name": "Legal Consultant",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Provides specialist legal research, opinions, and advisory services to clients and organizations.",
        "is_active": True,
    },
    {
        "id": "legal_associate",
        "name": "Legal Associate",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Supports legal teams with research, drafting, case preparation, and client matters.",
        "is_active": True,
    },
    {
        "id": "legal_researcher",
        "name": "Legal Researcher",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Researches legislation, case law, legal precedents, and regulatory developments.",
        "is_active": True,
    },
    {
        "id": "paralegal",
        "name": "Paralegal",
        "professional_field_id": "legal_compliance",
        "subfield_id": "legal_practice_advisory",
        "description": "Assists legal professionals with case preparation, legal documentation, research, and administration.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 2. Corporate & Commercial Law
    # --------------------------------------------------------
    {
        "id": "corporate_lawyer",
        "name": "Corporate Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises businesses on corporate structures, governance, transactions, and company law.",
        "is_active": True,
    },
    {
        "id": "commercial_lawyer",
        "name": "Commercial Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Handles legal matters involving commercial transactions, business relationships, and trade.",
        "is_active": True,
    },
    {
        "id": "corporate_legal_counsel",
        "name": "Corporate Legal Counsel",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Provides in-house legal advice on corporate matters, business decisions, and organizational risk.",
        "is_active": True,
    },
    {
        "id": "mergers_acquisitions_lawyer",
        "name": "Mergers and Acquisitions Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises on mergers, acquisitions, company restructuring, and related transaction documentation.",
        "is_active": True,
    },
    {
        "id": "securities_lawyer",
        "name": "Securities Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises on securities laws, capital market transactions, disclosures, and investor regulations.",
        "is_active": True,
    },
    {
        "id": "banking_lawyer",
        "name": "Banking Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Handles legal matters involving banking operations, lending, financial institutions, and banking regulations.",
        "is_active": True,
    },
    {
        "id": "capital_markets_lawyer",
        "name": "Capital Markets Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises on public offerings, securities issuance, capital raising, and capital market regulations.",
        "is_active": True,
    },
    {
        "id": "corporate_governance_lawyer",
        "name": "Corporate Governance Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises companies on board responsibilities, shareholder rights, and corporate governance law.",
        "is_active": True,
    },
    {
        "id": "business_legal_advisor",
        "name": "Business Legal Advisor",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises businesses on legal implications of commercial decisions, operations, and business arrangements.",
        "is_active": True,
    },
    {
        "id": "commercial_contracts_lawyer",
        "name": "Commercial Contracts Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Drafts, reviews, and negotiates commercial agreements and contractual arrangements.",
        "is_active": True,
    },
    {
        "id": "competition_lawyer",
        "name": "Competition Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises on competition law, market conduct, mergers, and fair competition requirements.",
        "is_active": True,
    },
    {
        "id": "antitrust_lawyer",
        "name": "Antitrust Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Handles antitrust matters involving monopolies, cartels, market competition, and enforcement.",
        "is_active": True,
    },
    {
        "id": "international_trade_lawyer",
        "name": "International Trade Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Advises on international trade regulations, cross-border transactions, tariffs, and trade disputes.",
        "is_active": True,
    },
    {
        "id": "corporate_legal_manager",
        "name": "Corporate Legal Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "corporate_commercial_law",
        "description": "Manages corporate legal functions, legal teams, business advisory, and organizational legal matters.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 3. Regulatory Affairs & Compliance
    # --------------------------------------------------------
    {
        "id": "legal_regulatory_affairs_specialist",
        "name": "Legal Regulatory Affairs Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Monitors legal and regulatory developments and advises organizations on regulatory obligations.",
        "is_active": True,
    },
    {
        "id": "regulatory_compliance_officer",
        "name": "Regulatory Compliance Officer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Monitors regulatory compliance and ensures organizational activities meet applicable legal requirements.",
        "is_active": True,
    },
    {
        "id": "regulatory_compliance_manager",
        "name": "Regulatory Compliance Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Manages regulatory compliance programs, controls, reporting, and regulatory obligations.",
        "is_active": True,
    },
    {
        "id": "regulatory_analyst",
        "name": "Regulatory Analyst",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Analyzes regulatory requirements, policy changes, and their impact on organizational operations.",
        "is_active": True,
    },
    {
        "id": "legal_regulatory_affairs_manager",
        "name": "Legal Regulatory Affairs Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Leads legal regulatory affairs activities, regulatory strategy, submissions, and stakeholder coordination.",
        "is_active": True,
    },
    {
        "id": "legal_regulatory_submissions_specialist",
        "name": "Legal Regulatory Submissions Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Coordinates regulatory filings, legal submissions, supporting documentation, and submission deadlines.",
        "is_active": True,
    },
    {
        "id": "regulatory_operations_specialist",
        "name": "Regulatory Operations Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Coordinates regulatory processes, documentation, tracking systems, and operational compliance activities.",
        "is_active": True,
    },
    {
        "id": "licensing_compliance_specialist",
        "name": "Licensing Compliance Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Ensures required licenses, permits, registrations, and renewals comply with applicable regulations.",
        "is_active": True,
    },
    {
        "id": "regulatory_inspector",
        "name": "Regulatory Inspector",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Inspects organizations and activities to assess compliance with laws, standards, and regulations.",
        "is_active": True,
    },
    {
        "id": "compliance_analyst",
        "name": "Compliance Analyst",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Reviews compliance data, identifies regulatory gaps, and supports compliance monitoring and reporting.",
        "is_active": True,
    },
    {
        "id": "compliance_officer",
        "name": "Compliance Officer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Implements compliance policies and monitors adherence to applicable laws and organizational requirements.",
        "is_active": True,
    },
    {
        "id": "compliance_manager",
        "name": "Compliance Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Leads compliance programs, risk assessments, internal controls, and regulatory reporting activities.",
        "is_active": True,
    },
    {
        "id": "legal_compliance_auditor",
        "name": "Legal Compliance Auditor",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Audits legal and regulatory compliance controls, policies, records, and organizational practices.",
        "is_active": True,
    },
    {
        "id": "regulatory_strategy_specialist",
        "name": "Regulatory Strategy Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "regulatory_affairs_compliance",
        "description": "Develops regulatory strategies and advises on regulatory pathways, changes, and compliance planning.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 4. Governance, Ethics & Corporate Compliance
    # --------------------------------------------------------
    {
        "id": "corporate_governance_specialist",
        "name": "Corporate Governance Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Supports corporate governance frameworks, board processes, policies, and governance reporting.",
        "is_active": True,
    },
    {
        "id": "governance_manager",
        "name": "Governance Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Manages governance frameworks, oversight processes, accountability structures, and governance controls.",
        "is_active": True,
    },
    {
        "id": "ethics_officer",
        "name": "Ethics Officer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Promotes ethical conduct and manages ethics policies, guidance, and organizational reporting channels.",
        "is_active": True,
    },
    {
        "id": "business_ethics_specialist",
        "name": "Business Ethics Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Advises on ethical business practices, conduct standards, and responsible organizational decision-making.",
        "is_active": True,
    },
    {
        "id": "corporate_compliance_specialist",
        "name": "Corporate Compliance Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Supports enterprise compliance policies, corporate controls, internal monitoring, and compliance initiatives.",
        "is_active": True,
    },
    {
        "id": "compliance_director",
        "name": "Compliance Director",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Directs organization-wide compliance strategy, governance, regulatory oversight, and compliance teams.",
        "is_active": True,
    },
    {
        "id": "chief_compliance_officer",
        "name": "Chief Compliance Officer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Provides executive leadership for enterprise compliance, regulatory obligations, and ethical conduct programs.",
        "is_active": True,
    },
    {
        "id": "enterprise_compliance_manager",
        "name": "Enterprise Compliance Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Coordinates enterprise-wide compliance frameworks, risk controls, monitoring, and remediation programs.",
        "is_active": True,
    },
    {
        "id": "anti_bribery_compliance_specialist",
        "name": "Anti-Bribery Compliance Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Implements anti-bribery and anti-corruption controls, assessments, training, and monitoring.",
        "is_active": True,
    },
    {
        "id": "anti_money_laundering_specialist",
        "name": "Anti-Money Laundering Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Supports anti-money laundering controls, transaction monitoring, investigations, and regulatory compliance.",
        "is_active": True,
    },
    {
        "id": "financial_crime_compliance_officer",
        "name": "Financial Crime Compliance Officer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Monitors financial crime risks and implements controls addressing fraud, sanctions, and illicit finance.",
        "is_active": True,
    },
    {
        "id": "conduct_risk_specialist",
        "name": "Conduct Risk Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Identifies and manages risks arising from employee, management, and organizational conduct.",
        "is_active": True,
    },
    {
        "id": "whistleblower_program_manager",
        "name": "Whistleblower Program Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Manages whistleblower reporting channels, case processes, investigations, and protection frameworks.",
        "is_active": True,
    },
    {
        "id": "corporate_integrity_officer",
        "name": "Corporate Integrity Officer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "governance_ethics_corporate_compliance",
        "description": "Promotes corporate integrity through ethical standards, investigations, and integrity controls.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 5. Contracts & Legal Operations
    # --------------------------------------------------------
    {
        "id": "contract_manager",
        "name": "Contract Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Manages contract lifecycle activities, negotiations, approvals, obligations, and renewals.",
        "is_active": True,
    },
    {
        "id": "contracts_administrator",
        "name": "Contracts Administrator",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Administers contract records, documentation, approvals, amendments, and contractual workflows.",
        "is_active": True,
    },
    {
        "id": "contracts_specialist",
        "name": "Contracts Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Supports contract drafting, review, negotiation, compliance, and lifecycle administration.",
        "is_active": True,
    },
    {
        "id": "contract_analyst",
        "name": "Contract Analyst",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Analyzes contract terms, obligations, risks, performance, and contractual data.",
        "is_active": True,
    },
    {
        "id": "contract_negotiation_specialist",
        "name": "Contract Negotiation Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Negotiates contractual terms and commercial conditions to achieve acceptable legal and business outcomes.",
        "is_active": True,
    },
    {
        "id": "legal_operations_manager",
        "name": "Legal Operations Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Manages legal department operations, budgets, technology, processes, and service delivery.",
        "is_active": True,
    },
    {
        "id": "legal_operations_analyst",
        "name": "Legal Operations Analyst",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Analyzes legal department performance, workflows, spending, and operational efficiency.",
        "is_active": True,
    },
    {
        "id": "legal_project_manager",
        "name": "Legal Project Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Plans and coordinates legal projects, matter delivery, resources, timelines, and stakeholder communication.",
        "is_active": True,
    },
    {
        "id": "legal_process_analyst",
        "name": "Legal Process Analyst",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Evaluates legal workflows and identifies opportunities to improve efficiency, consistency, and service quality.",
        "is_active": True,
    },
    {
        "id": "legal_billing_specialist",
        "name": "Legal Billing Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Manages legal billing, invoice review, timekeeping records, and matter-related financial administration.",
        "is_active": True,
    },
    {
        "id": "legal_documentation_specialist",
        "name": "Legal Documentation Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Prepares, organizes, reviews, and maintains legal documents and matter records.",
        "is_active": True,
    },
    {
        "id": "legal_secretary",
        "name": "Legal Secretary",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Provides administrative and document support to legal professionals and legal departments.",
        "is_active": True,
    },
    {
        "id": "legal_executive_assistant",
        "name": "Legal Executive Assistant",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Provides executive administrative support to legal leaders, including scheduling and confidential coordination.",
        "is_active": True,
    },
    {
        "id": "matter_management_specialist",
        "name": "Matter Management Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "contracts_legal_operations",
        "description": "Coordinates legal matters, case records, matter workflows, deadlines, and reporting.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 6. Intellectual Property & Privacy Law
    # --------------------------------------------------------
    {
        "id": "intellectual_property_lawyer",
        "name": "Intellectual Property Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Advises on intellectual property rights, protection, enforcement, and related legal disputes.",
        "is_active": True,
    },
    {
        "id": "patent_attorney",
        "name": "Patent Attorney",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Advises on patent law, patent applications, prosecution, and intellectual property disputes.",
        "is_active": True,
    },
    {
        "id": "patent_agent",
        "name": "Patent Agent",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Prepares and prosecutes patent applications and supports patent-related procedures where authorized.",
        "is_active": True,
    },
    {
        "id": "trademark_lawyer",
        "name": "Trademark Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Advises on trademark registration, protection, licensing, enforcement, and disputes.",
        "is_active": True,
    },
    {
        "id": "copyright_lawyer",
        "name": "Copyright Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Handles copyright protection, licensing, infringement, and related intellectual property matters.",
        "is_active": True,
    },
    {
        "id": "ip_legal_counsel",
        "name": "Intellectual Property Legal Counsel",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Provides legal guidance on intellectual property portfolios, licensing, protection, and commercial use.",
        "is_active": True,
    },
    {
        "id": "ip_licensing_specialist",
        "name": "IP Licensing Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Manages intellectual property licensing agreements, rights, negotiations, and compliance obligations.",
        "is_active": True,
    },
    {
        "id": "ip_portfolio_manager",
        "name": "IP Portfolio Manager",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Manages intellectual property portfolios, registrations, renewals, protection strategies, and reporting.",
        "is_active": True,
    },
    {
        "id": "ip_analyst",
        "name": "IP Analyst",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Analyzes intellectual property assets, patent landscapes, ownership, and portfolio information.",
        "is_active": True,
    },
    {
        "id": "patent_analyst",
        "name": "Patent Analyst",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Researches and analyzes patent filings, technology landscapes, claims, and prior art.",
        "is_active": True,
    },
    {
        "id": "privacy_lawyer",
        "name": "Privacy Lawyer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Advises on privacy laws, personal data rights, data processing, and privacy-related legal matters.",
        "is_active": True,
    },
    {
        "id": "data_privacy_counsel",
        "name": "Data Privacy Counsel",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Provides legal guidance on data privacy requirements, data governance, and privacy risk management.",
        "is_active": True,
    },
    {
        "id": "data_protection_officer",
        "name": "Data Protection Officer",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Oversees data protection compliance, privacy governance, and organizational data protection responsibilities.",
        "is_active": True,
    },
    {
        "id": "privacy_compliance_specialist",
        "name": "Privacy Compliance Specialist",
        "professional_field_id": "legal_compliance",
        "subfield_id": "intellectual_property_privacy_law",
        "description": "Implements and monitors privacy compliance controls, assessments, policies, and data protection procedures.",
        "is_active": True,
    },

])


# ============================================================
# DESIGN, ARTS & CREATIVE — 98 CANONICAL ROLES
# ============================================================

CANONICAL_ROLES.extend([

    # --------------------------------------------------------
    # 1. Graphic & Visual Design
    # --------------------------------------------------------
    {
        "id": "graphic_designer",
        "name": "Graphic Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Creates visual designs for digital and print media, marketing materials, and brand communication.",
        "is_active": True,
    },
    {
        "id": "visual_communication_designer",
        "name": "Visual Communication Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Develops visual communication concepts using typography, imagery, layout, and graphic design.",
        "is_active": True,
    },
    {
        "id": "brand_identity_designer",
        "name": "Brand Identity Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Creates visual brand identities including logos, color systems, typography, and brand guidelines.",
        "is_active": True,
    },
    {
        "id": "visual_design_specialist",
        "name": "Visual Design Specialist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Produces visual assets and design compositions for brand, marketing, and communication projects.",
        "is_active": True,
    },
    {
        "id": "publication_designer",
        "name": "Publication Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Designs layouts and visual systems for books, magazines, reports, and other publications.",
        "is_active": True,
    },
    {
        "id": "packaging_designer",
        "name": "Packaging Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Designs product packaging, labels, and packaging graphics that balance brand identity and usability.",
        "is_active": True,
    },
    {
        "id": "digital_graphic_designer",
        "name": "Digital Graphic Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Creates graphic assets for websites, digital campaigns, social media, and online platforms.",
        "is_active": True,
    },
    {
        "id": "marketing_graphic_designer",
        "name": "Marketing Graphic Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Produces promotional graphics and visual materials for advertising and marketing campaigns.",
        "is_active": True,
    },
    {
        "id": "print_designer",
        "name": "Print Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Creates designs for printed materials including brochures, posters, stationery, and promotional items.",
        "is_active": True,
    },
    {
        "id": "presentation_designer",
        "name": "Presentation Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Designs professional presentations, pitch decks, and visual storytelling materials.",
        "is_active": True,
    },
    {
        "id": "infographic_designer",
        "name": "Infographic Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Transforms information and data into clear, engaging visual explanations and infographics.",
        "is_active": True,
    },
    {
        "id": "creative_artworker",
        "name": "Creative Artworker",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Prepares and adapts creative artwork for production across digital and print formats.",
        "is_active": True,
    },
    {
        "id": "prepress_designer",
        "name": "Prepress Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Prepares and checks print-ready artwork, layouts, color settings, and production files.",
        "is_active": True,
    },
    {
        "id": "design_production_artist",
        "name": "Design Production Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "graphic_visual_design",
        "description": "Executes and adapts approved visual designs into accurate production-ready creative assets.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 2. UI/UX & Digital Product Design
    # --------------------------------------------------------
    {
        "id": "ui_ux_designer",
        "name": "UI/UX Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Designs user interfaces and experiences for websites, applications, and digital products.",
        "is_active": True,
    },
    {
        "id": "ux_designer",
        "name": "UX Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Designs intuitive digital experiences through user journeys, wireframes, prototyping, and usability evaluation.",
        "is_active": True,
    },
    {
        "id": "ui_designer",
        "name": "UI Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Creates interface layouts, visual components, typography, and interaction states for digital products.",
        "is_active": True,
    },
    {
        "id": "digital_product_designer",
        "name": "Digital Product Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Designs end-to-end digital product experiences by combining user research, interaction, and interface design.",
        "is_active": True,
    },
    {
        "id": "ux_researcher",
        "name": "UX Researcher",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Studies user behavior and needs through interviews, usability tests, surveys, and research analysis.",
        "is_active": True,
    },
    {
        "id": "interaction_designer",
        "name": "Interaction Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Designs interactive behaviors, user flows, transitions, and interface responses in digital products.",
        "is_active": True,
    },
    {
        "id": "service_designer",
        "name": "Service Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Designs connected service experiences across digital and physical customer touchpoints.",
        "is_active": True,
    },
    {
        "id": "user_research_specialist",
        "name": "User Research Specialist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Plans and conducts user research to identify needs, behaviors, and opportunities for product improvement.",
        "is_active": True,
    },
    {
        "id": "design_systems_designer",
        "name": "Design Systems Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Builds and maintains reusable design components, visual standards, and design system documentation.",
        "is_active": True,
    },
    {
        "id": "accessibility_designer",
        "name": "Accessibility Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Improves digital product accessibility through inclusive design practices and accessibility standards.",
        "is_active": True,
    },
    {
        "id": "information_architect",
        "name": "Information Architect",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Organizes digital content, navigation structures, and information systems for effective user discovery.",
        "is_active": True,
    },
    {
        "id": "usability_specialist",
        "name": "Usability Specialist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Evaluates digital interfaces and workflows to identify usability issues and improve user effectiveness.",
        "is_active": True,
    },
    {
        "id": "experience_design_lead",
        "name": "Experience Design Lead",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Leads experience design strategy, design quality, and collaboration across digital product teams.",
        "is_active": True,
    },
    {
        "id": "digital_interface_designer",
        "name": "Digital Interface Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "ui_ux_digital_product_design",
        "description": "Designs visual interfaces and responsive layouts for websites, applications, and digital platforms.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 3. Animation, Motion Graphics & 3D
    # --------------------------------------------------------
    {
        "id": "animator",
        "name": "Animator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Creates animated sequences and visual movement for films, games, advertisements, and digital media.",
        "is_active": True,
    },
    {
        "id": "two_d_animator",
        "name": "2D Animator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Creates two-dimensional animations for entertainment, advertising, educational, and digital content.",
        "is_active": True,
    },
    {
        "id": "three_d_animator",
        "name": "3D Animator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Creates three-dimensional character and object animation for films, games, and visual media.",
        "is_active": True,
    },
    {
        "id": "motion_graphics_designer",
        "name": "Motion Graphics Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Creates animated graphic elements, titles, visual effects, and motion-based communication content.",
        "is_active": True,
    },
    {
        "id": "three_d_modeler",
        "name": "3D Modeler",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Builds three-dimensional digital models of characters, objects, environments, and products.",
        "is_active": True,
    },
    {
        "id": "three_d_artist",
        "name": "3D Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Creates three-dimensional visual assets, scenes, and rendered artwork for digital media and entertainment.",
        "is_active": True,
    },
    {
        "id": "character_animator",
        "name": "Character Animator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Animates digital or drawn characters to convey movement, personality, and storytelling.",
        "is_active": True,
    },
    {
        "id": "character_designer",
        "name": "Character Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Develops character concepts, appearances, expressions, and visual styles for animated and interactive media.",
        "is_active": True,
    },
    {
        "id": "visual_effects_artist",
        "name": "Visual Effects Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Creates digital visual effects and computer-generated imagery for film, television, and digital production.",
        "is_active": True,
    },
    {
        "id": "compositor",
        "name": "Compositor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Combines visual layers, footage, effects, and digital elements into finished production shots.",
        "is_active": True,
    },
    {
        "id": "rigging_artist",
        "name": "Rigging Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Builds digital skeletons, controls, and deformation systems for animated characters and objects.",
        "is_active": True,
    },
    {
        "id": "storyboard_artist",
        "name": "Storyboard Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Visualizes scenes and sequences through storyboard illustrations for animation and screen production.",
        "is_active": True,
    },
    {
        "id": "technical_artist",
        "name": "Technical Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Bridges art and technology by developing tools, workflows, and technical solutions for creative production.",
        "is_active": True,
    },
    {
        "id": "animation_director",
        "name": "Animation Director",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "animation_motion_graphics_3d",
        "description": "Leads animation production, creative direction, visual consistency, and animation teams.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 4. Film, Video & Photography
    # --------------------------------------------------------
    {
        "id": "videographer",
        "name": "Videographer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Captures and produces video content for events, organizations, advertising, and digital platforms.",
        "is_active": True,
    },
    {
        "id": "video_editor",
        "name": "Video Editor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Edits video footage, audio, graphics, and transitions into finished video productions.",
        "is_active": True,
    },
    {
        "id": "film_editor",
        "name": "Film Editor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Shapes film narratives by selecting, arranging, and refining footage and recorded scenes.",
        "is_active": True,
    },
    {
        "id": "cinematographer",
        "name": "Cinematographer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Plans and oversees the visual capture of films and video productions through camera and lighting techniques.",
        "is_active": True,
    },
    {
        "id": "director_of_photography",
        "name": "Director of Photography",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Leads cinematography and visual storytelling, including camera, lighting, and image composition.",
        "is_active": True,
    },
    {
        "id": "film_director",
        "name": "Film Director",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Leads the creative execution of film productions, guiding performances, scenes, and visual storytelling.",
        "is_active": True,
    },
    {
        "id": "film_producer",
        "name": "Film Producer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Oversees film production planning, budgets, resources, coordination, and delivery.",
        "is_active": True,
    },
    {
        "id": "camera_operator",
        "name": "Camera Operator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Operates cameras and recording equipment to capture footage according to production requirements.",
        "is_active": True,
    },
    {
        "id": "photographer",
        "name": "Photographer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Captures and produces photographs for commercial, editorial, artistic, and documentary purposes.",
        "is_active": True,
    },
    {
        "id": "commercial_photographer",
        "name": "Commercial Photographer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Creates commissioned photography for advertising, products, brands, and commercial clients.",
        "is_active": True,
    },
    {
        "id": "photo_editor",
        "name": "Photo Editor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Selects, edits, retouches, and prepares photographs for publication and commercial use.",
        "is_active": True,
    },
    {
        "id": "colorist",
        "name": "Colorist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Performs color grading and correction to establish visual consistency and mood in video productions.",
        "is_active": True,
    },
    {
        "id": "production_designer_film",
        "name": "Film Production Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Develops the visual environment and overall production design for film and screen projects.",
        "is_active": True,
    },
    {
        "id": "post_production_supervisor",
        "name": "Post-Production Supervisor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "film_video_photography",
        "description": "Coordinates post-production workflows, schedules, resources, and delivery of film and video projects.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 5. Writing, Editing & Publishing
    # --------------------------------------------------------
    {
        "id": "creative_writer",
        "name": "Creative Writer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Creates original written works, narratives, and creative content across different formats.",
        "is_active": True,
    },
    {
        "id": "editorial_writer",
        "name": "Editorial Writer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Writes editorial articles, opinion pieces, features, and commentary for publications.",
        "is_active": True,
    },
    {
        "id": "technical_writer",
        "name": "Technical Writer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Creates technical documentation, user guides, manuals, and instructional content.",
        "is_active": True,
    },
    {
        "id": "copy_editor",
        "name": "Copy Editor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Reviews written content for grammar, clarity, consistency, accuracy, and editorial style.",
        "is_active": True,
    },
    {
        "id": "manuscript_editor",
        "name": "Manuscript Editor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Edits manuscripts for structure, readability, language, consistency, and publication readiness.",
        "is_active": True,
    },
    {
        "id": "proofreader",
        "name": "Proofreader",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Checks written and published materials for spelling, grammar, punctuation, and formatting errors.",
        "is_active": True,
    },
    {
        "id": "book_editor",
        "name": "Book Editor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Edits book manuscripts and works with authors to improve structure, content, and publication quality.",
        "is_active": True,
    },
    {
        "id": "publishing_editor",
        "name": "Publishing Editor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Manages editorial development and content quality for books and other publishing projects.",
        "is_active": True,
    },
    {
        "id": "editorial_content_specialist",
        "name": "Editorial Content Specialist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Develops, reviews, and refines editorial content to meet publication standards and audience needs.",
        "is_active": True,
    },
    {
        "id": "scriptwriter",
        "name": "Scriptwriter",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Writes scripts for video, television, digital media, advertising, and other productions.",
        "is_active": True,
    },
    {
        "id": "screenwriter",
        "name": "Screenwriter",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Develops screenplays and narrative scripts for films, television, and streaming productions.",
        "is_active": True,
    },
    {
        "id": "author",
        "name": "Author",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Writes books and other original literary or non-fiction works for publication.",
        "is_active": True,
    },
    {
        "id": "journalist",
        "name": "Journalist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Researches, verifies, and reports news and information through print and digital media.",
        "is_active": True,
    },
    {
        "id": "publishing_manager",
        "name": "Publishing Manager",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "writing_editing_publishing",
        "description": "Oversees publishing operations, editorial schedules, production workflows, and publication delivery.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 6. Fashion, Textile & Interior Design
    # --------------------------------------------------------
    {
        "id": "fashion_designer",
        "name": "Fashion Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Creates clothing and fashion collections through concept development, design, and material selection.",
        "is_active": True,
    },
    {
        "id": "fashion_illustrator",
        "name": "Fashion Illustrator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Produces fashion illustrations and visual concepts for apparel collections and design communication.",
        "is_active": True,
    },
    {
        "id": "textile_designer",
        "name": "Textile Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Creates textile patterns, surface designs, and fabric concepts for fashion and interior applications.",
        "is_active": True,
    },
    {
        "id": "fashion_merchandiser",
        "name": "Fashion Merchandiser",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Coordinates fashion product ranges, assortment planning, trends, and merchandising requirements.",
        "is_active": True,
    },
    {
        "id": "fashion_stylist",
        "name": "Fashion Stylist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Creates clothing and accessory combinations for campaigns, editorial shoots, events, and clients.",
        "is_active": True,
    },
    {
        "id": "costume_designer",
        "name": "Costume Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Designs costumes and wardrobe concepts for film, television, theatre, and performance productions.",
        "is_active": True,
    },
    {
        "id": "apparel_technical_designer",
        "name": "Apparel Technical Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Develops garment specifications, technical packs, fit requirements, and construction details.",
        "is_active": True,
    },
    {
        "id": "pattern_maker",
        "name": "Pattern Maker",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Creates and adjusts garment patterns for apparel construction and production.",
        "is_active": True,
    },
    {
        "id": "interior_designer",
        "name": "Interior Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Plans and designs interior environments, including layouts, materials, furnishings, and finishes.",
        "is_active": True,
    },
    {
        "id": "interior_decorator",
        "name": "Interior Decorator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Selects furnishings, colors, fabrics, accessories, and decorative elements for interior spaces.",
        "is_active": True,
    },
    {
        "id": "interior_space_planner",
        "name": "Interior Space Planner",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Plans interior layouts and space utilization to improve functionality, circulation, and spatial efficiency.",
        "is_active": True,
    },
    {
        "id": "furniture_designer",
        "name": "Furniture Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Designs furniture products by combining functionality, materials, ergonomics, and visual aesthetics.",
        "is_active": True,
    },
    {
        "id": "set_designer",
        "name": "Set Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Designs physical or digital sets and environments for film, television, theatre, and events.",
        "is_active": True,
    },
    {
        "id": "sustainable_fashion_designer",
        "name": "Sustainable Fashion Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fashion_textile_interior_design",
        "description": "Develops fashion products using sustainable materials, responsible production methods, and circular design principles.",
        "is_active": True,
    },

    # --------------------------------------------------------
    # 7. Fine Arts, Illustration & Creative Direction
    # --------------------------------------------------------
    {
        "id": "fine_artist",
        "name": "Fine Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Creates original artworks using traditional or contemporary artistic mediums and techniques.",
        "is_active": True,
    },
    {
        "id": "illustrator",
        "name": "Illustrator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Creates illustrations for books, publications, advertising, entertainment, and digital media.",
        "is_active": True,
    },
    {
        "id": "digital_illustrator",
        "name": "Digital Illustrator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Produces original illustrations and visual artwork using digital drawing and painting tools.",
        "is_active": True,
    },
    {
        "id": "concept_artist",
        "name": "Concept Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Develops visual concepts, characters, environments, and objects for games, films, and creative projects.",
        "is_active": True,
    },
    {
        "id": "portrait_artist",
        "name": "Portrait Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Creates artistic portraits of individuals or groups using traditional or digital media.",
        "is_active": True,
    },
    {
        "id": "visual_artist",
        "name": "Visual Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Produces visual artworks and creative concepts across a range of artistic media and disciplines.",
        "is_active": True,
    },
    {
        "id": "art_director",
        "name": "Art Director",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Leads visual direction and creative execution across advertising, publishing, media, and design projects.",
        "is_active": True,
    },
    {
        "id": "creative_director",
        "name": "Creative Director",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Leads overall creative strategy, concepts, and execution across creative teams and projects.",
        "is_active": True,
    },
    {
        "id": "creative_designer",
        "name": "Creative Designer",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Develops creative visual concepts and design assets across brand, marketing, and media projects.",
        "is_active": True,
    },
    {
        "id": "mural_artist",
        "name": "Mural Artist",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Creates large-scale artworks and painted designs for walls and public or private spaces.",
        "is_active": True,
    },
    {
        "id": "sculptor",
        "name": "Sculptor",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Creates three-dimensional artworks using materials such as stone, metal, wood, clay, and mixed media.",
        "is_active": True,
    },
    {
        "id": "painter",
        "name": "Painter",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Creates paintings and visual artworks using traditional or contemporary painting techniques.",
        "is_active": True,
    },
    {
        "id": "printmaker",
        "name": "Printmaker",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Creates original artwork through printmaking processes such as etching, lithography, and screen printing.",
        "is_active": True,
    },
    {
        "id": "art_curator",
        "name": "Art Curator",
        "professional_field_id": "design_arts_creative",
        "subfield_id": "fine_arts_illustration_creative_direction",
        "description": "Selects, researches, organizes, and presents artworks and exhibitions for galleries and cultural institutions.",
        "is_active": True,
    },

])



CANONICAL_ROLES.extend([
    # ============================================================
    # HOSPITALITY & RETAIL & SKILLED TRADES
    # ============================================================

    # 1. HOSPITALITY & HOTEL MANAGEMENT
    {
        "id": "hotel_general_manager",
        "name": "Hotel General Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Leads overall hotel operations, business performance, staffing, guest satisfaction, and service standards.",
        "is_active": True
    },
    {
        "id": "hotel_operations_manager",
        "name": "Hotel Operations Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Coordinates daily hotel operations across departments to maintain service quality and operational efficiency.",
        "is_active": True
    },
    {
        "id": "front_office_manager",
        "name": "Front Office Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Manages hotel reception, reservations, check-in and check-out, and front desk personnel.",
        "is_active": True
    },
    {
        "id": "front_desk_receptionist",
        "name": "Front Desk Receptionist",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Welcomes hotel guests, handles check-in and check-out, responds to enquiries, and manages reception duties.",
        "is_active": True
    },
    {
        "id": "guest_relations_executive",
        "name": "Guest Relations Executive",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Assists hotel guests, handles service requests, resolves concerns, and improves the guest experience.",
        "is_active": True
    },
    {
        "id": "hotel_concierge",
        "name": "Hotel Concierge",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Provides guests with local information, recommendations, bookings, and personalized assistance.",
        "is_active": True
    },
    {
        "id": "hotel_reservations_agent",
        "name": "Hotel Reservations Agent",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Handles room bookings, reservation enquiries, availability checks, and booking modifications.",
        "is_active": True
    },
    {
        "id": "housekeeping_manager",
        "name": "Housekeeping Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Oversees housekeeping operations, room cleanliness, staff scheduling, and hotel hygiene standards.",
        "is_active": True
    },
    {
        "id": "housekeeping_supervisor",
        "name": "Housekeeping Supervisor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Supervises housekeeping staff, room preparation, cleaning schedules, and quality inspections.",
        "is_active": True
    },
    {
        "id": "hotel_room_attendant",
        "name": "Hotel Room Attendant",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Cleans and prepares guest rooms, replenishes supplies, and maintains housekeeping standards.",
        "is_active": True
    },
    {
        "id": "hotel_revenue_manager",
        "name": "Hotel Revenue Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Optimizes room pricing, occupancy, demand forecasting, and revenue performance.",
        "is_active": True
    },
    {
        "id": "hotel_guest_services_manager",
        "name": "Hotel Guest Services Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Manages guest-facing services and coordinates teams to maintain a consistent guest experience.",
        "is_active": True
    },
    {
        "id": "hotel_night_auditor",
        "name": "Hotel Night Auditor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Handles overnight reception duties, reconciles daily accounts, and prepares hotel financial reports.",
        "is_active": True
    },
    {
        "id": "hotel_banquet_manager",
        "name": "Hotel Banquet Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "hospitality_hotel_management",
        "description": "Plans and manages hotel banquets, functions, event service teams, and banquet operations.",
        "is_active": True
    },

    # 2. FOOD & BEVERAGE SERVICES
    {
        "id": "restaurant_manager",
        "name": "Restaurant Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Manages restaurant operations, staff, customer service, budgets, and service standards.",
        "is_active": True
    },
    {
        "id": "assistant_restaurant_manager",
        "name": "Assistant Restaurant Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Supports restaurant management by supervising daily service, employees, and customer experience.",
        "is_active": True
    },
    {
        "id": "food_beverage_manager",
        "name": "Food and Beverage Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Oversees food and beverage operations, service teams, budgets, and hospitality standards.",
        "is_active": True
    },
    {
        "id": "food_beverage_supervisor",
        "name": "Food and Beverage Supervisor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Supervises food and beverage service staff and ensures efficient daily service delivery.",
        "is_active": True
    },
    {
        "id": "restaurant_server",
        "name": "Restaurant Server",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Takes customer orders, serves food and beverages, and supports dining service operations.",
        "is_active": True
    },
    {
        "id": "bartender",
        "name": "Bartender",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Prepares and serves beverages, manages bar service, and maintains bar equipment and supplies.",
        "is_active": True
    },
    {
        "id": "barista",
        "name": "Barista",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Prepares and serves coffee, espresso-based drinks, and other beverages in cafes and restaurants.",
        "is_active": True
    },
    {
        "id": "sommelier",
        "name": "Sommelier",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Advises customers on wine selection, food pairings, wine service, and beverage programs.",
        "is_active": True
    },
    {
        "id": "restaurant_host",
        "name": "Restaurant Host",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Welcomes diners, manages seating arrangements, handles reservations, and coordinates guest flow.",
        "is_active": True
    },
    {
        "id": "catering_manager",
        "name": "Catering Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Manages catering services, food preparation arrangements, event requirements, and catering teams.",
        "is_active": True
    },
    {
        "id": "catering_coordinator",
        "name": "Catering Coordinator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Coordinates catering bookings, menus, suppliers, logistics, and event service arrangements.",
        "is_active": True
    },
    {
        "id": "banquet_server",
        "name": "Banquet Server",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Serves food and beverages at banquets, conferences, weddings, and other organized functions.",
        "is_active": True
    },
    {
        "id": "room_service_attendant",
        "name": "Room Service Attendant",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Delivers food and beverage orders to hotel guests and maintains room service standards.",
        "is_active": True
    },
    {
        "id": "food_service_supervisor",
        "name": "Food Service Supervisor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "food_beverage_services",
        "description": "Supervises food service teams and daily operations in restaurants, cafeterias, and institutional kitchens.",
        "is_active": True
    },

    # 3. TRAVEL, TOURISM & EVENT SERVICES
    {
        "id": "travel_agent",
        "name": "Travel Agent",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Arranges travel bookings, transportation, accommodation, and holiday packages for customers.",
        "is_active": True
    },
    {
        "id": "travel_consultant",
        "name": "Travel Consultant",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Advises customers on destinations, itineraries, travel arrangements, and suitable holiday options.",
        "is_active": True
    },
    {
        "id": "tour_operator",
        "name": "Tour Operator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Organizes and operates tours, travel packages, destination activities, and group travel services.",
        "is_active": True
    },
    {
        "id": "tour_guide",
        "name": "Tour Guide",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Guides visitors through destinations, attractions, and cultural or historical sites.",
        "is_active": True
    },
    {
        "id": "travel_coordinator",
        "name": "Travel Coordinator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Coordinates travel schedules, bookings, itineraries, and logistical arrangements for individuals or groups.",
        "is_active": True
    },
    {
        "id": "travel_operations_manager",
        "name": "Travel Operations Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Oversees travel service operations, supplier relationships, bookings, and operational performance.",
        "is_active": True
    },
    {
        "id": "tourism_manager",
        "name": "Tourism Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Manages tourism programs, visitor services, destination promotion, and tourism operations.",
        "is_active": True
    },
    {
        "id": "destination_manager",
        "name": "Destination Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Coordinates destination development, visitor experiences, tourism partners, and destination services.",
        "is_active": True
    },
    {
        "id": "event_planner",
        "name": "Event Planner",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Plans event concepts, schedules, budgets, venues, suppliers, and event logistics.",
        "is_active": True
    },
    {
        "id": "event_coordinator",
        "name": "Event Coordinator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Coordinates event schedules, vendors, bookings, logistics, and on-site arrangements.",
        "is_active": True
    },
    {
        "id": "event_manager",
        "name": "Event Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Manages event planning and delivery, budgets, teams, suppliers, and client requirements.",
        "is_active": True
    },
    {
        "id": "conference_manager",
        "name": "Conference Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Organizes conferences and business events, coordinating venues, speakers, schedules, and services.",
        "is_active": True
    },
    {
        "id": "wedding_planner",
        "name": "Wedding Planner",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Plans and coordinates wedding events, vendors, ceremonies, receptions, and client requirements.",
        "is_active": True
    },
    {
        "id": "event_production_coordinator",
        "name": "Event Production Coordinator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "travel_tourism_event_services",
        "description": "Coordinates event staging, production schedules, technical suppliers, equipment, and production logistics.",
        "is_active": True
    },

    # 4. RETAIL & STORE OPERATIONS
    {
        "id": "retail_store_manager",
        "name": "Retail Store Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Manages store operations, employees, sales performance, inventory, and customer service standards.",
        "is_active": True
    },
    {
        "id": "assistant_store_manager",
        "name": "Assistant Store Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Supports store management and supervises daily retail operations, staff, and customer service.",
        "is_active": True
    },
    {
        "id": "retail_department_manager",
        "name": "Retail Department Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Manages a retail department, including employees, merchandise, inventory, and department performance.",
        "is_active": True
    },
    {
        "id": "retail_department_supervisor",
        "name": "Retail Department Supervisor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Supervises department employees, merchandise presentation, stock availability, and daily retail activities.",
        "is_active": True
    },
    {
        "id": "retail_operations_manager",
        "name": "Retail Operations Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Oversees retail operational processes, store performance, procedures, and multi-location execution.",
        "is_active": True
    },
    {
        "id": "retail_operations_coordinator",
        "name": "Retail Operations Coordinator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Coordinates store procedures, operational reporting, schedules, and retail support activities.",
        "is_active": True
    },
    {
        "id": "retail_cashier",
        "name": "Retail Cashier",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Processes customer purchases, payments, refunds, and transactions at retail checkout counters.",
        "is_active": True
    },
    {
        "id": "checkout_operator",
        "name": "Checkout Operator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Operates checkout systems, scans merchandise, processes payments, and assists customers during checkout.",
        "is_active": True
    },
    {
        "id": "retail_stock_associate",
        "name": "Retail Stock Associate",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Receives, organizes, replenishes, and maintains merchandise stock in retail stores.",
        "is_active": True
    },
    {
        "id": "retail_inventory_associate",
        "name": "Retail Inventory Associate",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Tracks retail inventory, performs stock counts, and maintains accurate inventory records.",
        "is_active": True
    },
    {
        "id": "retail_receiving_clerk",
        "name": "Retail Receiving Clerk",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Receives incoming merchandise, verifies deliveries, records stock, and coordinates goods handling.",
        "is_active": True
    },
    {
        "id": "retail_inventory_controller",
        "name": "Retail Inventory Controller",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Controls inventory accuracy, stock movements, replenishment processes, and inventory reporting.",
        "is_active": True
    },
    {
        "id": "retail_replenishment_associate",
        "name": "Retail Replenishment Associate",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Replenishes shelves, maintains product availability, and organizes merchandise displays.",
        "is_active": True
    },
    {
        "id": "retail_buyer",
        "name": "Retail Buyer",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "retail_store_operations",
        "description": "Selects and purchases retail merchandise, negotiates supplier terms, and manages product assortments.",
        "is_active": True
    },

    # 5. CULINARY ARTS & FOOD PRODUCTION
    {
        "id": "executive_chef",
        "name": "Executive Chef",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Leads kitchen operations, develops menus, manages culinary teams, and maintains food quality standards.",
        "is_active": True
    },
    {
        "id": "head_chef",
        "name": "Head Chef",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Leads kitchen staff, supervises food preparation, and ensures consistent culinary standards.",
        "is_active": True
    },
    {
        "id": "sous_chef",
        "name": "Sous Chef",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Assists the head chef and supervises kitchen operations, food preparation, and culinary staff.",
        "is_active": True
    },
    {
        "id": "chef_de_partie",
        "name": "Chef de Partie",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Manages a specific kitchen station and prepares dishes according to established culinary standards.",
        "is_active": True
    },
    {
        "id": "commis_chef",
        "name": "Commis Chef",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Supports senior chefs with food preparation, basic cooking, and kitchen organization.",
        "is_active": True
    },
    {
        "id": "line_cook",
        "name": "Line Cook",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Prepares and cooks menu items at an assigned kitchen station during service.",
        "is_active": True
    },
    {
        "id": "prep_cook",
        "name": "Prep Cook",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Prepares ingredients, portions food, and supports kitchen readiness before service.",
        "is_active": True
    },
    {
        "id": "pastry_chef",
        "name": "Pastry Chef",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Creates pastries, desserts, and baked products while managing pastry preparation and presentation.",
        "is_active": True
    },
    {
        "id": "professional_baker",
        "name": "Professional Baker",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Produces breads, cakes, pastries, and other baked goods for commercial or retail operations.",
        "is_active": True
    },
    {
        "id": "cake_decorator",
        "name": "Cake Decorator",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Decorates cakes and confectionery products using icing, fondant, and other finishing techniques.",
        "is_active": True
    },
    {
        "id": "butcher",
        "name": "Butcher",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Cuts, prepares, and portions meat products for retail, food service, or commercial production.",
        "is_active": True
    },
    {
        "id": "fishmonger",
        "name": "Fishmonger",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Selects, prepares, cuts, and sells fish and seafood while maintaining freshness and hygiene standards.",
        "is_active": True
    },
    {
        "id": "food_production_supervisor",
        "name": "Food Production Supervisor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Supervises food production teams, preparation processes, output quality, and production schedules.",
        "is_active": True
    },
    {
        "id": "kitchen_manager",
        "name": "Kitchen Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "culinary_arts_food_production",
        "description": "Manages kitchen staffing, food preparation, supplies, hygiene, and daily kitchen operations.",
        "is_active": True
    },

    # 6. CONSTRUCTION & BUILDING TRADES
    {
        "id": "construction_foreman",
        "name": "Construction Foreman",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Directs construction crews, assigns tasks, monitors work progress, and enforces site safety.",
        "is_active": True
    },
    {
        "id": "construction_site_supervisor",
        "name": "Construction Site Supervisor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Supervises on-site construction activities, workers, materials, schedules, and safety procedures.",
        "is_active": True
    },
    {
        "id": "carpenter",
        "name": "Carpenter",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Constructs, installs, and repairs wooden structures, fixtures, frameworks, and fittings.",
        "is_active": True
    },
    {
        "id": "mason",
        "name": "Mason",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Builds and repairs structures using brick, stone, concrete blocks, and other masonry materials.",
        "is_active": True
    },
    {
        "id": "bricklayer",
        "name": "Bricklayer",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Lays bricks and blocks to construct walls, partitions, foundations, and other structures.",
        "is_active": True
    },
    {
        "id": "plasterer",
        "name": "Plasterer",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Applies plaster and finishing materials to walls, ceilings, and other building surfaces.",
        "is_active": True
    },
    {
        "id": "roofer",
        "name": "Roofer",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Installs, repairs, and maintains roofs, roofing materials, and weatherproofing systems.",
        "is_active": True
    },
    {
        "id": "construction_painter",
        "name": "Construction Painter",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Prepares and paints building interiors, exteriors, and construction surfaces.",
        "is_active": True
    },
    {
        "id": "tile_setter",
        "name": "Tile Setter",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Installs ceramic, stone, and other tiles on floors, walls, and building surfaces.",
        "is_active": True
    },
    {
        "id": "drywall_installer",
        "name": "Drywall Installer",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Installs drywall panels, partitions, and ceiling systems in building projects.",
        "is_active": True
    },
    {
        "id": "glazier",
        "name": "Glazier",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Measures, cuts, installs, and repairs glass in windows, doors, and building structures.",
        "is_active": True
    },
    {
        "id": "flooring_installer",
        "name": "Flooring Installer",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Installs and repairs flooring materials including tiles, wood, laminate, and resilient flooring.",
        "is_active": True
    },
    {
        "id": "scaffolder",
        "name": "Scaffolder",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Erects, modifies, and dismantles scaffolding systems for construction and maintenance work.",
        "is_active": True
    },
    {
        "id": "concrete_finisher",
        "name": "Concrete Finisher",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "construction_building_trades",
        "description": "Pours, levels, smooths, and finishes concrete surfaces for construction projects.",
        "is_active": True
    },

    # 7. ELECTRICAL, PLUMBING & MECHANICAL TRADES
    {
        "id": "electrician",
        "name": "Electrician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs, maintains, and repairs electrical wiring, equipment, circuits, and power systems.",
        "is_active": True
    },
    {
        "id": "electrical_technician",
        "name": "Electrical Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Tests, maintains, troubleshoots, and repairs electrical equipment and control systems.",
        "is_active": True
    },
    {
        "id": "plumber",
        "name": "Plumber",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs, maintains, and repairs water supply, drainage, sanitation, and plumbing systems.",
        "is_active": True
    },
    {
        "id": "pipefitter",
        "name": "Pipefitter",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Fabricates, installs, and maintains industrial piping systems and associated equipment.",
        "is_active": True
    },
    {
        "id": "hvac_technician",
        "name": "HVAC Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs, services, and repairs heating, ventilation, and air conditioning systems.",
        "is_active": True
    },
    {
        "id": "refrigeration_technician",
        "name": "Refrigeration Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs and maintains commercial and industrial refrigeration and cooling equipment.",
        "is_active": True
    },
    {
        "id": "appliance_repair_technician",
        "name": "Appliance Repair Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Diagnoses and repairs household and commercial electrical and mechanical appliances.",
        "is_active": True
    },
    {
        "id": "industrial_maintenance_technician",
        "name": "Industrial Maintenance Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Maintains and repairs industrial machinery, production equipment, and mechanical systems.",
        "is_active": True
    },
    {
        "id": "welder",
        "name": "Welder",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Joins and repairs metal components using welding processes and fabrication techniques.",
        "is_active": True
    },
    {
        "id": "elevator_technician",
        "name": "Elevator Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs, inspects, maintains, and repairs elevators and lifting equipment.",
        "is_active": True
    },
    {
        "id": "solar_panel_installer",
        "name": "Solar Panel Installer",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs and maintains solar photovoltaic panels, mounting systems, and related equipment.",
        "is_active": True
    },
    {
        "id": "fire_alarm_technician",
        "name": "Fire Alarm Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs, tests, inspects, and maintains fire alarm and detection systems.",
        "is_active": True
    },
    {
        "id": "building_automation_technician",
        "name": "Building Automation Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Installs and maintains automated building control systems for lighting, climate, and equipment.",
        "is_active": True
    },
    {
        "id": "sheet_metal_worker",
        "name": "Sheet Metal Worker",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "electrical_plumbing_mechanical_trades",
        "description": "Fabricates, assembles, installs, and repairs sheet metal products and ductwork.",
        "is_active": True
    },

    # 8. AUTOMOTIVE, REPAIR & MAINTENANCE SERVICES
    {
        "id": "automotive_service_technician",
        "name": "Automotive Service Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Services, inspects, and repairs vehicles through scheduled maintenance and mechanical diagnostics.",
        "is_active": True
    },
    {
        "id": "auto_mechanic",
        "name": "Auto Mechanic",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Diagnoses, repairs, and maintains vehicle engines, mechanical systems, and components.",
        "is_active": True
    },
    {
        "id": "diesel_mechanic",
        "name": "Diesel Mechanic",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Maintains and repairs diesel engines and vehicles such as trucks, buses, and heavy equipment.",
        "is_active": True
    },
    {
        "id": "motorcycle_mechanic",
        "name": "Motorcycle Mechanic",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Services and repairs motorcycles, scooters, engines, and related mechanical systems.",
        "is_active": True
    },
    {
        "id": "auto_electrician",
        "name": "Auto Electrician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Diagnoses and repairs vehicle electrical wiring, batteries, lighting, and electronic systems.",
        "is_active": True
    },
    {
        "id": "vehicle_diagnostics_technician",
        "name": "Vehicle Diagnostics Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Uses diagnostic equipment to identify faults in vehicle mechanical, electrical, and electronic systems.",
        "is_active": True
    },
    {
        "id": "automotive_service_advisor",
        "name": "Automotive Service Advisor",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Advises vehicle owners on repairs, maintenance requirements, service estimates, and workshop services.",
        "is_active": True
    },
    {
        "id": "automotive_service_manager",
        "name": "Automotive Service Manager",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Manages automotive service centers, workshop teams, repair schedules, and customer service operations.",
        "is_active": True
    },
    {
        "id": "auto_body_repair_technician",
        "name": "Auto Body Repair Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Repairs damaged vehicle body panels, frames, and exterior components after accidents or wear.",
        "is_active": True
    },
    {
        "id": "automotive_painter",
        "name": "Automotive Painter",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Prepares and paints vehicle surfaces, applies coatings, and performs automotive paint finishing.",
        "is_active": True
    },
    {
        "id": "tire_service_technician",
        "name": "Tire Service Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Inspects, installs, repairs, and replaces vehicle tires and related wheel components.",
        "is_active": True
    },
    {
        "id": "wheel_alignment_technician",
        "name": "Wheel Alignment Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Measures and adjusts vehicle wheel alignment, steering geometry, and suspension settings.",
        "is_active": True
    },
    {
        "id": "vehicle_inspector",
        "name": "Vehicle Inspector",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Inspects vehicle condition, safety, and compliance with required inspection standards.",
        "is_active": True
    },
    {
        "id": "fleet_maintenance_technician",
        "name": "Fleet Maintenance Technician",
        "professional_field_id": "hospitality_retail_skilled_trades",
        "subfield_id": "automotive_repair_maintenance_services",
        "description": "Maintains and repairs vehicles in commercial fleets to ensure safety, reliability, and availability.",
        "is_active": True
    }
])




def get_professional_fields():
    """Return the master list of professional fields."""
    return PROFESSIONAL_FIELDS


def get_subfields_by_field(field_id: str):
    """Return subfields belonging to a professional field."""
    return SUBFIELDS_BY_FIELD.get(field_id, [])


# ============================================================
# ROLE ALIASES
# ============================================================


# ============================================================
# ROLE ALIASES — TECHNOLOGY & IT
# ============================================================

ROLE_ALIASES = [

    # --------------------------------------------------------
    # 1. Artificial Intelligence & Generative AI
    # --------------------------------------------------------
    {"alias": "Artificial Intelligence Developer", "canonical_role_id": "ai_application_developer", "is_active": True},
    {"alias": "GenAI Engineer", "canonical_role_id": "generative_ai_engineer", "is_active": True},
    {"alias": "GenAI Developer", "canonical_role_id": "generative_ai_engineer", "is_active": True},
    {"alias": "LLM Developer", "canonical_role_id": "llm_engineer", "is_active": True},
    {"alias": "Large Language Model Developer", "canonical_role_id": "llm_engineer", "is_active": True},
    {"alias": "Prompt Designer", "canonical_role_id": "prompt_engineer", "is_active": True},
    {"alias": "Chatbot Engineer", "canonical_role_id": "conversational_ai_engineer", "is_active": True},
    {"alias": "AI Agent Engineer", "canonical_role_id": "ai_agent_developer", "is_active": True},
    {"alias": "AI Systems Architect", "canonical_role_id": "ai_architect", "is_active": True},
    {"alias": "Responsible AI Specialist", "canonical_role_id": "responsible_ai_engineer", "is_active": True},

    # --------------------------------------------------------
    # 2. Machine Learning & Deep Learning
    # --------------------------------------------------------
    {"alias": "ML Engineer", "canonical_role_id": "machine_learning_engineer", "is_active": True},
    {"alias": "ML Developer", "canonical_role_id": "machine_learning_engineer", "is_active": True},
    {"alias": "Deep Neural Network Engineer", "canonical_role_id": "deep_learning_engineer", "is_active": True},
    {"alias": "Applied ML Engineer", "canonical_role_id": "applied_machine_learning_engineer", "is_active": True},
    {"alias": "ML Researcher", "canonical_role_id": "machine_learning_research_engineer", "is_active": True},
    {"alias": "Computer Vision Developer", "canonical_role_id": "computer_vision_engineer", "is_active": True},
    {"alias": "NLP Developer", "canonical_role_id": "nlp_engineer", "is_active": True},
    {"alias": "Reinforcement Learning (RL) Engineer", "canonical_role_id": "reinforcement_learning_engineer", "is_active": True},
    {"alias": "MLOps Specialist", "canonical_role_id": "mlops_engineer", "is_active": True},
    {"alias": "Recommendation Engine Engineer", "canonical_role_id": "recommendation_systems_engineer", "is_active": True},

    # --------------------------------------------------------
    # 3. Data Science & Applied AI
    # --------------------------------------------------------
    {"alias": "Data Science Developer", "canonical_role_id": "data_science_engineer", "is_active": True},
    {"alias": "Applied AI Developer", "canonical_role_id": "applied_ai_engineer", "is_active": True},
    {"alias": "Predictive Analytics Scientist", "canonical_role_id": "predictive_modeling_scientist", "is_active": True},
    {"alias": "Computer Vision Research Scientist", "canonical_role_id": "computer_vision_scientist", "is_active": True},
    {"alias": "Natural Language Processing Scientist", "canonical_role_id": "nlp_scientist", "is_active": True},

    # --------------------------------------------------------
    # 4. Software Development
    # --------------------------------------------------------
    {"alias": "Software Programmer", "canonical_role_id": "software_developer", "is_active": True},
    {"alias": "Application Programmer", "canonical_role_id": "application_developer", "is_active": True},
    {"alias": "Systems Programmer", "canonical_role_id": "systems_software_engineer", "is_active": True},
    {"alias": "Desktop Software Developer", "canonical_role_id": "desktop_application_developer", "is_active": True},
    {"alias": "API Programmer", "canonical_role_id": "api_developer", "is_active": True},
    {"alias": "Game Programmer", "canonical_role_id": "game_developer", "is_active": True},
    {"alias": "Distributed Systems Developer", "canonical_role_id": "distributed_systems_engineer", "is_active": True},
    {"alias": "Software Integration Specialist", "canonical_role_id": "software_integration_engineer", "is_active": True},

    # --------------------------------------------------------
    # 5. Frontend Development
    # --------------------------------------------------------
    {"alias": "ReactJS Developer", "canonical_role_id": "react_developer", "is_active": True},
    {"alias": "React.js Engineer", "canonical_role_id": "react_developer", "is_active": True},
    {"alias": "Angular Frontend Developer", "canonical_role_id": "angular_developer", "is_active": True},
    {"alias": "Vue.js Engineer", "canonical_role_id": "vuejs_developer", "is_active": True},
    {"alias": "JavaScript Frontend Developer", "canonical_role_id": "javascript_developer", "is_active": True},
    {"alias": "TypeScript Frontend Developer", "canonical_role_id": "typescript_developer", "is_active": True},
    {"alias": "User Interface Developer", "canonical_role_id": "ui_developer", "is_active": True},
    {"alias": "Web UI Developer", "canonical_role_id": "web_ui_engineer", "is_active": True},

    # --------------------------------------------------------
    # 6. Backend Development
    # --------------------------------------------------------
    {"alias": "Server-Side Developer", "canonical_role_id": "backend_developer", "is_active": True},
    {"alias": "Server-Side Engineer", "canonical_role_id": "backend_engineer", "is_active": True},
    {"alias": "Python Server-Side Developer", "canonical_role_id": "python_developer", "is_active": True},
    {"alias": "Python Backend Developer", "canonical_role_id": "python_developer", "is_active": True},
    {"alias": "Python Backend Engineer", "canonical_role_id": "python_developer", "is_active": True},
    {"alias": "Backend Python Developer", "canonical_role_id": "python_developer", "is_active": True},
    {"alias": "Java Backend Developer", "canonical_role_id": "java_developer", "is_active": True},
    {"alias": "Java Backend Engineer", "canonical_role_id": "java_developer", "is_active": True},
    {"alias": ".NET Backend Developer", "canonical_role_id": "dotnet_developer", "is_active": True},
    {"alias": "PHP Backend Developer", "canonical_role_id": "php_developer", "is_active": True},
    {"alias": "PHP Backend Engineer", "canonical_role_id": "php_developer", "is_active": True},
    {"alias": "Go Backend Developer", "canonical_role_id": "go_developer", "is_active": True},
    {"alias": "Go Backend Engineer", "canonical_role_id": "go_developer", "is_active": True},
    {"alias": "Node.js Backend Developer", "canonical_role_id": "nodejs_developer", "is_active": True},

    {"alias": "Java Server-Side Developer", "canonical_role_id": "java_developer", "is_active": True},
    {"alias": "Node.js Backend Engineer", "canonical_role_id": "nodejs_developer", "is_active": True},
    {"alias": "ASP.NET Backend Developer", "canonical_role_id": "dotnet_developer", "is_active": True},
    {"alias": "PHP Server-Side Developer", "canonical_role_id": "php_developer", "is_active": True},
    {"alias": "Golang Backend Developer", "canonical_role_id": "go_developer", "is_active": True},
    {"alias": "REST API Engineer", "canonical_role_id": "api_engineer", "is_active": True},
    {"alias": "Microservices Developer", "canonical_role_id": "microservices_engineer", "is_active": True},

    # --------------------------------------------------------
    # 7. Full Stack Development
    # --------------------------------------------------------
    {"alias": "Fullstack Developer", "canonical_role_id": "full_stack_developer", "is_active": True},
    {"alias": "Fullstack Engineer", "canonical_role_id": "full_stack_engineer", "is_active": True},
    {"alias": "MERN Stack Engineer", "canonical_role_id": "mern_stack_developer", "is_active": True},
    {"alias": "MEAN Stack Engineer", "canonical_role_id": "mean_stack_developer", "is_active": True},
    {"alias": "Java Fullstack Engineer", "canonical_role_id": "java_full_stack_developer", "is_active": True},
    {"alias": "Python Fullstack Engineer", "canonical_role_id": "python_full_stack_developer", "is_active": True},
    {"alias": "JavaScript Fullstack Developer", "canonical_role_id": "javascript_full_stack_developer", "is_active": True},

    # --------------------------------------------------------
    # 8. Mobile Application Development
    # --------------------------------------------------------
    {"alias": "Android App Developer", "canonical_role_id": "android_developer", "is_active": True},
    {"alias": "iPhone Application Developer", "canonical_role_id": "ios_developer", "is_active": True},
    {"alias": "iOS App Engineer", "canonical_role_id": "ios_developer", "is_active": True},
    {"alias": "React Native Engineer", "canonical_role_id": "react_native_developer", "is_active": True},
    {"alias": "Flutter App Developer", "canonical_role_id": "flutter_developer", "is_active": True},
    {"alias": "Kotlin Android Developer", "canonical_role_id": "kotlin_developer", "is_active": True},
    {"alias": "Swift iOS Developer", "canonical_role_id": "swift_developer", "is_active": True},
    {"alias": "Cross-Platform App Developer", "canonical_role_id": "cross_platform_mobile_developer", "is_active": True},

    # --------------------------------------------------------
    # 9. Web Development
    # --------------------------------------------------------
    {"alias": "Website Developer", "canonical_role_id": "web_developer", "is_active": True},
    {"alias": "Website Engineer", "canonical_role_id": "web_engineer", "is_active": True},
    {"alias": "WordPress Engineer", "canonical_role_id": "wordpress_developer", "is_active": True},
    {"alias": "CMS Programmer", "canonical_role_id": "cms_developer", "is_active": True},
    {"alias": "Ecommerce Web Developer", "canonical_role_id": "ecommerce_developer", "is_active": True},
    {"alias": "Web App Developer", "canonical_role_id": "web_application_developer", "is_active": True},
    {"alias": "Website Designer Developer", "canonical_role_id": "web_designer_developer", "is_active": True},
    {"alias": "Web Speed Optimization Engineer", "canonical_role_id": "web_performance_engineer", "is_active": True},
    {"alias": "Web Accessibility Specialist", "canonical_role_id": "web_accessibility_engineer", "is_active": True},

    # --------------------------------------------------------
    # 10. Cloud Computing & Architecture
    # --------------------------------------------------------
    {"alias": "AWS Engineer", "canonical_role_id": "aws_cloud_engineer", "is_active": True},
    {"alias": "Azure Engineer", "canonical_role_id": "azure_cloud_engineer", "is_active": True},
    {"alias": "GCP Engineer", "canonical_role_id": "google_cloud_engineer", "is_active": True},
    {"alias": "Cloud Infrastructure Specialist", "canonical_role_id": "cloud_infrastructure_engineer", "is_active": True},
    {"alias": "Cloud Platform Specialist", "canonical_role_id": "cloud_platform_engineer", "is_active": True},
    {"alias": "Cloud Migration Specialist", "canonical_role_id": "cloud_migration_engineer", "is_active": True},
    {"alias": "Cloud Network Specialist", "canonical_role_id": "cloud_network_engineer", "is_active": True},

    # --------------------------------------------------------
    # 11. DevOps & Site Reliability Engineering
    # --------------------------------------------------------
    {"alias": "SRE Engineer", "canonical_role_id": "site_reliability_engineer", "is_active": True},
    {"alias": "Site Reliability (SRE) Specialist", "canonical_role_id": "site_reliability_engineer", "is_active": True},
    {"alias": "CI/CD Specialist", "canonical_role_id": "cicd_engineer", "is_active": True},
    {"alias": "Build and Release Specialist", "canonical_role_id": "build_release_engineer", "is_active": True},
    {"alias": "Infrastructure Automation Specialist", "canonical_role_id": "infrastructure_automation_engineer", "is_active": True},
    {"alias": "DevSecOps Specialist", "canonical_role_id": "devsecops_engineer", "is_active": True},
    {"alias": "Kubernetes Specialist", "canonical_role_id": "kubernetes_engineer", "is_active": True},
    {"alias": "Container Platform Engineer", "canonical_role_id": "containerization_engineer", "is_active": True},
    {"alias": "Observability Specialist", "canonical_role_id": "observability_engineer", "is_active": True},

    # --------------------------------------------------------
    # 12. Cybersecurity & Information Security
    # --------------------------------------------------------
    {"alias": "InfoSec Analyst", "canonical_role_id": "information_security_analyst", "is_active": True},
    {"alias": "AppSec Engineer", "canonical_role_id": "application_security_engineer", "is_active": True},
    {"alias": "Ethical Hacker", "canonical_role_id": "penetration_tester", "is_active": True},
    {"alias": "Pen Tester", "canonical_role_id": "penetration_tester", "is_active": True},
    {"alias": "SOC Security Analyst", "canonical_role_id": "soc_analyst", "is_active": True},
    {"alias": "Incident Response Specialist", "canonical_role_id": "incident_response_engineer", "is_active": True},
    {"alias": "IAM Engineer", "canonical_role_id": "identity_access_management_engineer", "is_active": True},
    {"alias": "Vulnerability Analyst", "canonical_role_id": "vulnerability_management_engineer", "is_active": True},
    {"alias": "Information Security Consultant", "canonical_role_id": "security_consultant", "is_active": True},

    # --------------------------------------------------------
    # 13. Networking & Infrastructure
    # --------------------------------------------------------
    {"alias": "Sysadmin", "canonical_role_id": "systems_administrator", "is_active": True},
    {"alias": "Network Ops Center Engineer", "canonical_role_id": "noc_engineer", "is_active": True},
    {"alias": "Wireless Systems Engineer", "canonical_role_id": "wireless_network_engineer", "is_active": True},
    {"alias": "Telecom Engineer", "canonical_role_id": "telecommunications_engineer", "is_active": True},
    {"alias": "Data Centre Engineer", "canonical_role_id": "data_center_engineer", "is_active": True},
    {"alias": "IT Infrastructure Specialist", "canonical_role_id": "infrastructure_engineer", "is_active": True},

    # --------------------------------------------------------
    # 14. Database & Data Administration
    # --------------------------------------------------------
    {"alias": "DBA", "canonical_role_id": "database_administrator", "is_active": True},
    {"alias": "DB Administrator", "canonical_role_id": "database_administrator", "is_active": True},
    {"alias": "DB Developer", "canonical_role_id": "database_developer", "is_active": True},
    {"alias": "DB Architect", "canonical_role_id": "database_architect", "is_active": True},
    {"alias": "NoSQL Engineer", "canonical_role_id": "nosql_database_engineer", "is_active": True},
    {"alias": "Database SRE", "canonical_role_id": "database_reliability_engineer", "is_active": True},
    {"alias": "Data Migration Specialist", "canonical_role_id": "data_migration_engineer", "is_active": True},
    {"alias": "Database Performance Specialist", "canonical_role_id": "database_performance_engineer", "is_active": True},

    # --------------------------------------------------------
    # 15. Software Testing & Quality Assurance
    # --------------------------------------------------------
    {"alias": "Software QA Engineer", "canonical_role_id": "qa_engineer", "is_active": True},
    {"alias": "Automation QA Engineer", "canonical_role_id": "automation_test_engineer", "is_active": True},
    {"alias": "Manual QA Tester", "canonical_role_id": "manual_test_engineer", "is_active": True},
    {"alias": "Software Test Automation Engineer", "canonical_role_id": "automation_test_engineer", "is_active": True},
    {"alias": "Performance QA Engineer", "canonical_role_id": "performance_test_engineer", "is_active": True},
    {"alias": "API QA Engineer", "canonical_role_id": "api_test_engineer", "is_active": True},
    {"alias": "QA Team Lead", "canonical_role_id": "test_lead", "is_active": True},
    {"alias": "Test Automation Architect", "canonical_role_id": "test_automation_architect", "is_active": True},

    # --------------------------------------------------------
    # 16. Embedded Systems & Firmware
    # --------------------------------------------------------
    {"alias": "Embedded Developer", "canonical_role_id": "embedded_software_engineer", "is_active": True},
    {"alias": "Firmware Programmer", "canonical_role_id": "firmware_developer", "is_active": True},
    {"alias": "Embedded Linux Developer", "canonical_role_id": "embedded_linux_engineer", "is_active": True},
    {"alias": "RTOS Developer", "canonical_role_id": "rtos_engineer", "is_active": True},
    {"alias": "IoT Software Engineer", "canonical_role_id": "iot_engineer", "is_active": True},
    {"alias": "Robotics Software Developer", "canonical_role_id": "robotics_software_engineer", "is_active": True},
    {"alias": "Automotive Embedded Software Developer", "canonical_role_id": "automotive_embedded_software_engineer", "is_active": True},

    # --------------------------------------------------------
    # 17. Hardware & Semiconductor Engineering
    # --------------------------------------------------------
    {"alias": "VLSI Engineer", "canonical_role_id": "vlsi_design_engineer", "is_active": True},
    {"alias": "ASIC Designer", "canonical_role_id": "asic_design_engineer", "is_active": True},
    {"alias": "FPGA Engineer", "canonical_role_id": "fpga_design_engineer", "is_active": True},
    {"alias": "PCB Layout Engineer", "canonical_role_id": "pcb_design_engineer", "is_active": True},
    {"alias": "Chip Design Specialist", "canonical_role_id": "chip_design_engineer", "is_active": True},
    {"alias": "Hardware Verification Specialist", "canonical_role_id": "verification_engineer", "is_active": True},
    {"alias": "Hardware Test Engineer", "canonical_role_id": "hardware_validation_engineer", "is_active": True},

    # --------------------------------------------------------
    # 18. Enterprise Applications & ERP
    # --------------------------------------------------------
    {"alias": "SAP ERP Consultant", "canonical_role_id": "sap_consultant", "is_active": True},
    {"alias": "SAP Application Developer", "canonical_role_id": "sap_developer", "is_active": True},
    {"alias": "Dynamics 365 Consultant", "canonical_role_id": "microsoft_dynamics_consultant", "is_active": True},
    {"alias": "Oracle ERP Consultant", "canonical_role_id": "oracle_applications_consultant", "is_active": True},
    {"alias": "CRM Software Developer", "canonical_role_id": "crm_developer", "is_active": True},
    {"alias": "ERP Functional Specialist", "canonical_role_id": "erp_functional_consultant", "is_active": True},
    {"alias": "ERP Technical Specialist", "canonical_role_id": "erp_technical_consultant", "is_active": True},

    # --------------------------------------------------------
    # 19. IT Support & Technical Services
    # --------------------------------------------------------
    {"alias": "IT Helpdesk Analyst", "canonical_role_id": "help_desk_analyst", "is_active": True},
    {"alias": "Helpdesk Technician", "canonical_role_id": "help_desk_analyst", "is_active": True},
    {"alias": "Desktop Support Technician", "canonical_role_id": "desktop_support_engineer", "is_active": True},
    {"alias": "Field IT Technician", "canonical_role_id": "it_field_support_engineer", "is_active": True},
    {"alias": "IT Operations Support Specialist", "canonical_role_id": "it_operations_support_engineer", "is_active": True},
    {"alias": "IT Support Team Manager", "canonical_role_id": "it_support_manager", "is_active": True},

    # --------------------------------------------------------
    # 20. IT Management & Architecture
    # --------------------------------------------------------
    {"alias": "Enterprise IT Architect", "canonical_role_id": "enterprise_architect", "is_active": True},
    {"alias": "IT Solutions Architect", "canonical_role_id": "solutions_architect", "is_active": True},
    {"alias": "Technology Architect", "canonical_role_id": "technical_architect", "is_active": True},
    {"alias": "ITSM Manager", "canonical_role_id": "it_service_management_manager", "is_active": True},
    {"alias": "IT Strategy Manager", "canonical_role_id": "technology_strategy_manager", "is_active": True},
    {"alias": "IT Governance Lead", "canonical_role_id": "it_governance_manager", "is_active": True},
]


# ============================================================
# ROLE ALIASES — DATA & ANALYTICS
# ============================================================

ROLE_ALIASES.extend([

    # --------------------------------------------------------
    # 1. Data Analysis & Reporting
    # --------------------------------------------------------
    {"alias": "Senior Data Reporting Analyst", "canonical_role_id": "senior_data_analyst", "is_active": True},
    {"alias": "MIS Reporting Analyst", "canonical_role_id": "mis_analyst", "is_active": True},
    {"alias": "Data Reporting Analyst", "canonical_role_id": "data_reporting_specialist", "is_active": True},
    {"alias": "Business Reporting Analyst", "canonical_role_id": "business_data_analyst", "is_active": True},
    {"alias": "Operations Reporting Analyst", "canonical_role_id": "operations_data_analyst", "is_active": True},
    {"alias": "Data Validation Analyst", "canonical_role_id": "data_quality_analyst", "is_active": True},
    {"alias": "Data Visualization Specialist", "canonical_role_id": "data_visualization_analyst", "is_active": True},
    {"alias": "Head of Data Analysis", "canonical_role_id": "data_analysis_manager", "is_active": True},

    # --------------------------------------------------------
    # 2. Business Intelligence & Visualization
    # --------------------------------------------------------
    {"alias": "BI Analyst", "canonical_role_id": "business_intelligence_analyst", "is_active": True},
    {"alias": "Business Intelligence (BI) Developer", "canonical_role_id": "business_intelligence_developer", "is_active": True},
    {"alias": "Business Intelligence Engineer", "canonical_role_id": "bi_engineer", "is_active": True},
    {"alias": "BI Solutions Consultant", "canonical_role_id": "bi_consultant", "is_active": True},
    {"alias": "Power BI Report Developer", "canonical_role_id": "power_bi_developer", "is_active": True},
    {"alias": "Tableau BI Developer", "canonical_role_id": "tableau_developer", "is_active": True},
    {"alias": "Data Visualization Engineer", "canonical_role_id": "data_visualization_developer", "is_active": True},
    {"alias": "BI Solutions Architect", "canonical_role_id": "business_intelligence_architect", "is_active": True},
    {"alias": "Business Intelligence Reporting Analyst", "canonical_role_id": "bi_reporting_analyst", "is_active": True},
    {"alias": "Head of Business Intelligence", "canonical_role_id": "business_intelligence_manager", "is_active": True},

    # --------------------------------------------------------
    # 3. Data Engineering
    # --------------------------------------------------------
    {"alias": "Senior Data Platform Engineer", "canonical_role_id": "senior_data_engineer", "is_active": True},
    {"alias": "ETL Programmer", "canonical_role_id": "etl_developer", "is_active": True},
    {"alias": "Data Pipeline Developer", "canonical_role_id": "data_pipeline_engineer", "is_active": True},
    {"alias": "Analytics Data Platform Engineer", "canonical_role_id": "analytics_data_engineer", "is_active": True},
    {"alias": "Cloud-Based Data Engineer", "canonical_role_id": "cloud_data_engineer", "is_active": True},
    {"alias": "Real-Time Data Streaming Engineer", "canonical_role_id": "streaming_data_engineer", "is_active": True},
    {"alias": "Data Integration Specialist", "canonical_role_id": "data_integration_engineer", "is_active": True},
    {"alias": "Data Engineering Architect", "canonical_role_id": "data_engineering_architect", "is_active": True},
    {"alias": "Data Platform Architect", "canonical_role_id": "data_platform_engineer", "is_active": True},
    {"alias": "Head of Data Engineering", "canonical_role_id": "data_engineering_manager", "is_active": True},

    # --------------------------------------------------------
    # 4. Big Data & Distributed Systems
    # --------------------------------------------------------
    {"alias": "Big Data Programmer", "canonical_role_id": "big_data_developer", "is_active": True},
    {"alias": "Hadoop Programmer", "canonical_role_id": "hadoop_developer", "is_active": True},
    {"alias": "Apache Spark Developer", "canonical_role_id": "spark_developer", "is_active": True},
    {"alias": "Big Data Solutions Architect", "canonical_role_id": "big_data_architect", "is_active": True},
    {"alias": "Data Streaming Developer", "canonical_role_id": "data_streaming_engineer", "is_active": True},
    {"alias": "Distributed Data Systems Engineer", "canonical_role_id": "distributed_data_engineer", "is_active": True},
    {"alias": "Big Data Infrastructure Engineer", "canonical_role_id": "big_data_platform_engineer", "is_active": True},
    {"alias": "Big Data Solutions Consultant", "canonical_role_id": "big_data_consultant", "is_active": True},

    # --------------------------------------------------------
    # 5. Data Warehousing & Architecture
    # --------------------------------------------------------
    {"alias": "Data Warehouse Developer", "canonical_role_id": "data_warehouse_developer", "is_active": True},
    {"alias": "Data Warehouse Architect", "canonical_role_id": "data_warehouse_architect", "is_active": True},
    {"alias": "Data Warehouse DBA", "canonical_role_id": "data_warehouse_administrator", "is_active": True},
    {"alias": "Data Modeling Specialist", "canonical_role_id": "data_modeling_engineer", "is_active": True},
    {"alias": "Data Modeling Analyst", "canonical_role_id": "data_modeler", "is_active": True},
    {"alias": "Cloud Data Warehouse Specialist", "canonical_role_id": "cloud_data_warehouse_engineer", "is_active": True},
    {"alias": "Data Warehouse Solutions Consultant", "canonical_role_id": "data_warehouse_consultant", "is_active": True},
    {"alias": "Data Warehouse ETL Specialist", "canonical_role_id": "data_warehouse_etl_developer", "is_active": True},
    {"alias": "Head of Data Warehousing", "canonical_role_id": "data_warehouse_manager", "is_active": True},

    # --------------------------------------------------------
    # 6. Business & Product Analytics
    # --------------------------------------------------------
    {"alias": "Business Systems Analyst", "canonical_role_id": "business_analyst", "is_active": True},
    {"alias": "Product Data Analyst", "canonical_role_id": "product_data_analyst", "is_active": True},
    {"alias": "Product Insights Analyst", "canonical_role_id": "product_analyst", "is_active": True},
    {"alias": "Growth Data Analyst", "canonical_role_id": "growth_analyst", "is_active": True},
    {"alias": "Customer Intelligence Analyst", "canonical_role_id": "customer_insights_analyst", "is_active": True},
    {"alias": "Business Intelligence Analytics Consultant", "canonical_role_id": "business_analytics_consultant", "is_active": True},
    {"alias": "Head of Product Analytics", "canonical_role_id": "product_analytics_manager", "is_active": True},
    {"alias": "Head of Business Analytics", "canonical_role_id": "business_analytics_manager", "is_active": True},
    {"alias": "Web Analytics Analyst", "canonical_role_id": "digital_analytics_analyst", "is_active": True},

    # --------------------------------------------------------
    # 7. Statistical & Quantitative Analytics
    # --------------------------------------------------------
    {"alias": "Applied Statistician", "canonical_role_id": "statistician", "is_active": True},
    {"alias": "Quant Analyst", "canonical_role_id": "quantitative_analyst", "is_active": True},
    {"alias": "Quantitative Research Analyst", "canonical_role_id": "quantitative_research_analyst", "is_active": True},
    {"alias": "Statistical Data Analyst", "canonical_role_id": "statistical_analyst", "is_active": True},
    {"alias": "Econometrics Analyst", "canonical_role_id": "econometrician", "is_active": True},
    {"alias": "Operations Research Specialist", "canonical_role_id": "operations_research_analyst", "is_active": True},
    {"alias": "Biological Statistician", "canonical_role_id": "biostatistician", "is_active": True},
    {"alias": "Head of Quantitative Analytics", "canonical_role_id": "quantitative_analytics_manager", "is_active": True},

    # --------------------------------------------------------
    # 8. Marketing, Financial & Operations Analytics
    # --------------------------------------------------------
    {"alias": "Marketing Data Analyst", "canonical_role_id": "marketing_analyst", "is_active": True},
    {"alias": "Financial Reporting Analyst", "canonical_role_id": "financial_data_analyst", "is_active": True},
    {"alias": "Business Financial Analyst", "canonical_role_id": "financial_analyst", "is_active": True},
    {"alias": "Supply Chain Data Analyst", "canonical_role_id": "supply_chain_analyst", "is_active": True},
    {"alias": "Sales Revenue Analyst", "canonical_role_id": "revenue_analyst", "is_active": True},
    {"alias": "Pricing Strategy Analyst", "canonical_role_id": "pricing_analyst", "is_active": True},
    {"alias": "Head of Marketing Analytics", "canonical_role_id": "marketing_analytics_manager", "is_active": True},
    {"alias": "Head of Financial Analytics", "canonical_role_id": "financial_analytics_manager", "is_active": True},
    {"alias": "Head of Operations Analytics", "canonical_role_id": "operations_analytics_manager", "is_active": True},

    # --------------------------------------------------------
    # 9. Data Governance & Quality
    # --------------------------------------------------------
    {"alias": "Data Governance Specialist", "canonical_role_id": "data_governance_analyst", "is_active": True},
    {"alias": "Head of Data Governance", "canonical_role_id": "data_governance_manager", "is_active": True},
    {"alias": "Data Stewardship Specialist", "canonical_role_id": "data_steward", "is_active": True},
    {"alias": "Data Quality Specialist", "canonical_role_id": "data_quality_engineer", "is_active": True},
    {"alias": "Head of Data Quality", "canonical_role_id": "data_quality_manager", "is_active": True},
    {"alias": "MDM Specialist", "canonical_role_id": "master_data_management_specialist", "is_active": True},
    {"alias": "Master Data Specialist", "canonical_role_id": "master_data_management_specialist", "is_active": True},
    {"alias": "Metadata Specialist", "canonical_role_id": "metadata_management_specialist", "is_active": True},
    {"alias": "Data Regulatory Compliance Analyst", "canonical_role_id": "data_compliance_analyst", "is_active": True},
    {"alias": "Data Governance Advisory Consultant", "canonical_role_id": "data_governance_consultant", "is_active": True},
    {"alias": "Data Management Team Lead", "canonical_role_id": "data_management_lead", "is_active": True},

    # --------------------------------------------------------
    # 10. Analytics Engineering & Data Management
    # --------------------------------------------------------
    {"alias": "Senior Analytics Developer", "canonical_role_id": "senior_analytics_engineer", "is_active": True},
    {"alias": "Analytics Solutions Architect", "canonical_role_id": "analytics_architect", "is_active": True},
    {"alias": "Analytics Software Developer", "canonical_role_id": "analytics_developer", "is_active": True},
    {"alias": "Analytics Infrastructure Engineer", "canonical_role_id": "analytics_platform_engineer", "is_active": True},
    {"alias": "Data Administration Specialist", "canonical_role_id": "data_management_specialist", "is_active": True},
    {"alias": "Data Management Advisory Consultant", "canonical_role_id": "data_management_consultant", "is_active": True},
    {"alias": "Head of Analytics Engineering", "canonical_role_id": "analytics_engineering_manager", "is_active": True},
    {"alias": "Data Solutions Architect", "canonical_role_id": "data_solutions_architect", "is_active": True},
    {"alias": "Analytics Solutions Specialist", "canonical_role_id": "analytics_solutions_engineer", "is_active": True},

])


# ============================================================
# ROLE ALIASES — ENGINEERING & MANUFACTURING
# ============================================================

ROLE_ALIASES.extend([

    # --------------------------------------------------------
    # 1. Mechanical Engineering
    # --------------------------------------------------------
    {"alias": "Mechanical Design Engineer", "canonical_role_id": "design_engineer", "is_active": True},
    {"alias": "Product Development Engineer", "canonical_role_id": "product_design_engineer", "is_active": True},
    {"alias": "Computer-Aided Design Engineer", "canonical_role_id": "cad_design_engineer", "is_active": True},
    {"alias": "Heating, Ventilation and Air Conditioning Engineer", "canonical_role_id": "hvac_engineer", "is_active": True},
    {"alias": "Thermal Systems Engineer", "canonical_role_id": "thermal_engineer", "is_active": True},
    {"alias": "Automotive Mechanical Design Engineer", "canonical_role_id": "automotive_mechanical_engineer", "is_active": True},
    {"alias": "Mechanical Project Design Engineer", "canonical_role_id": "mechanical_project_engineer", "is_active": True},
    {"alias": "Mechanical Maintenance Engineer", "canonical_role_id": "maintenance_mechanical_engineer", "is_active": True},
    {"alias": "Manufacturing Design Engineer", "canonical_role_id": "manufacturing_mechanical_engineer", "is_active": True},
    {"alias": "Mechanical Simulation Engineer", "canonical_role_id": "mechanical_analysis_engineer", "is_active": True},
    {"alias": "Head of Mechanical Engineering", "canonical_role_id": "mechanical_engineering_manager", "is_active": True},

    # --------------------------------------------------------
    # 2. Electrical & Electronics Engineering
    # --------------------------------------------------------
    {"alias": "Electrical Systems Engineer", "canonical_role_id": "electrical_engineer", "is_active": True},
    {"alias": "Electronics Design Engineer", "canonical_role_id": "electronics_engineer", "is_active": True},
    {"alias": "Electrical Systems Design Engineer", "canonical_role_id": "electrical_design_engineer", "is_active": True},
    {"alias": "Power Systems Design Engineer", "canonical_role_id": "power_systems_engineer", "is_active": True},
    {"alias": "Control and Automation Systems Engineer", "canonical_role_id": "control_systems_engineer", "is_active": True},
    {"alias": "Instrumentation and Control Engineer", "canonical_role_id": "instrumentation_engineer", "is_active": True},
    {"alias": "Electrical Service and Maintenance Engineer", "canonical_role_id": "electrical_maintenance_engineer", "is_active": True},
    {"alias": "Embedded Electronics Design Engineer", "canonical_role_id": "embedded_electronics_engineer", "is_active": True},
    {"alias": "Power Electronics Design Engineer", "canonical_role_id": "power_electronics_engineer", "is_active": True},
    {"alias": "Electrical Project Design Engineer", "canonical_role_id": "electrical_project_engineer", "is_active": True},
    {"alias": "Electronics Validation Engineer", "canonical_role_id": "electronics_test_engineer", "is_active": True},
    {"alias": "Head of Electrical Engineering", "canonical_role_id": "electrical_engineering_manager", "is_active": True},

    # --------------------------------------------------------
    # 3. Civil & Structural Engineering
    # --------------------------------------------------------
    {"alias": "Civil Construction Engineer", "canonical_role_id": "civil_engineer", "is_active": True},
    {"alias": "Structural Design Engineer", "canonical_role_id": "structural_engineer", "is_active": True},
    {"alias": "Construction Site Engineer", "canonical_role_id": "site_engineer", "is_active": True},
    {"alias": "Soil and Foundation Engineer", "canonical_role_id": "geotechnical_engineer", "is_active": True},
    {"alias": "Transportation Systems Engineer", "canonical_role_id": "transportation_engineer", "is_active": True},
    {"alias": "Roadway Design Engineer", "canonical_role_id": "highway_engineer", "is_active": True},
    {"alias": "Construction Quantity Surveyor", "canonical_role_id": "quantity_surveyor", "is_active": True},
    {"alias": "Building Information Modeling Engineer", "canonical_role_id": "bim_engineer", "is_active": True},
    {"alias": "Civil Construction Project Engineer", "canonical_role_id": "civil_project_engineer", "is_active": True},
    {"alias": "Head of Civil Engineering", "canonical_role_id": "civil_engineering_manager", "is_active": True},

    # --------------------------------------------------------
    # 4. Chemical & Process Engineering
    # --------------------------------------------------------
    {"alias": "Chemical Process Design Engineer", "canonical_role_id": "chemical_engineer", "is_active": True},
    {"alias": "Industrial Process Engineer", "canonical_role_id": "process_engineer", "is_active": True},
    {"alias": "Process Design and Development Engineer", "canonical_role_id": "process_design_engineer", "is_active": True},
    {"alias": "Process Risk and Safety Engineer", "canonical_role_id": "process_safety_engineer", "is_active": True},
    {"alias": "Chemical Production Engineer", "canonical_role_id": "chemical_process_engineer", "is_active": True},
    {"alias": "Production Process Design Engineer", "canonical_role_id": "production_process_engineer", "is_active": True},
    {"alias": "Petroleum and Petrochemical Engineer", "canonical_role_id": "petrochemical_engineer", "is_active": True},
    {"alias": "Process Automation and Control Engineer", "canonical_role_id": "process_control_engineer", "is_active": True},
    {"alias": "Chemical Process Project Engineer", "canonical_role_id": "chemical_project_engineer", "is_active": True},
    {"alias": "Head of Chemical Engineering", "canonical_role_id": "chemical_engineering_manager", "is_active": True},

    # --------------------------------------------------------
    # 5. Industrial & Production Engineering
    # --------------------------------------------------------
    {"alias": "Manufacturing Production Engineer", "canonical_role_id": "production_engineer", "is_active": True},
    {"alias": "Production Planning and Control Engineer", "canonical_role_id": "production_planning_engineer", "is_active": True},
    {"alias": "Manufacturing Process Development Engineer", "canonical_role_id": "manufacturing_engineer", "is_active": True},
    {"alias": "Lean Manufacturing Specialist", "canonical_role_id": "lean_manufacturing_engineer", "is_active": True},
    {"alias": "Process Improvement Engineer", "canonical_role_id": "continuous_improvement_engineer", "is_active": True},
    {"alias": "Production Scheduler", "canonical_role_id": "production_planner", "is_active": True},
    {"alias": "Industrial Controls Engineer", "canonical_role_id": "industrial_automation_engineer", "is_active": True},
    {"alias": "Manufacturing Process Development Specialist", "canonical_role_id": "manufacturing_process_engineer", "is_active": True},
    {"alias": "Production Line Supervisor", "canonical_role_id": "production_supervisor", "is_active": True},
    {"alias": "Head of Industrial Engineering", "canonical_role_id": "industrial_engineering_manager", "is_active": True},
    {"alias": "Manufacturing Production Manager", "canonical_role_id": "production_manager", "is_active": True},

    # --------------------------------------------------------
    # 6. Manufacturing Automation
    # --------------------------------------------------------
    {"alias": "PLC Controls Programmer", "canonical_role_id": "plc_programmer", "is_active": True},
    {"alias": "Supervisory Control and Data Acquisition Engineer", "canonical_role_id": "scada_engineer", "is_active": True},
    {"alias": "Industrial Automation Design Engineer", "canonical_role_id": "automation_design_engineer", "is_active": True},
    {"alias": "Industrial Automation Technician", "canonical_role_id": "automation_technician", "is_active": True},
    {"alias": "Head of Manufacturing Automation", "canonical_role_id": "manufacturing_automation_manager", "is_active": True},
    {"alias": "Automation Systems Project Engineer", "canonical_role_id": "automation_project_engineer", "is_active": True},

    # --------------------------------------------------------
    # 7. Automotive & Transportation Engineering
    # --------------------------------------------------------
    {"alias": "Automotive Systems Design Engineer", "canonical_role_id": "automotive_engineer", "is_active": True},
    {"alias": "Automotive Product Design Engineer", "canonical_role_id": "automotive_design_engineer", "is_active": True},
    {"alias": "Automotive Testing and Validation Engineer", "canonical_role_id": "automotive_validation_engineer", "is_active": True},
    {"alias": "Vehicle Performance Engineer", "canonical_role_id": "vehicle_dynamics_engineer", "is_active": True},
    {"alias": "Automotive Powertrain Systems Engineer", "canonical_role_id": "powertrain_engineer", "is_active": True},
    {"alias": "EV Engineer", "canonical_role_id": "electric_vehicle_engineer", "is_active": True},
    {"alias": "Automotive Systems Integration Engineer", "canonical_role_id": "automotive_systems_engineer", "is_active": True},
    {"alias": "Aeronautical Engineer", "canonical_role_id": "aerospace_engineer", "is_active": True},
    {"alias": "Transportation Systems Specialist", "canonical_role_id": "transportation_engineering_specialist", "is_active": True},
    {"alias": "Head of Automotive Engineering", "canonical_role_id": "automotive_engineering_manager", "is_active": True},

    # --------------------------------------------------------
    # 8. Materials & Metallurgical Engineering
    # --------------------------------------------------------
    {"alias": "Materials Development Engineer", "canonical_role_id": "materials_engineer", "is_active": True},
    {"alias": "Metallurgy Engineer", "canonical_role_id": "metallurgical_engineer", "is_active": True},
    {"alias": "Materials Research Scientist", "canonical_role_id": "materials_scientist", "is_active": True},
    {"alias": "Welding Process Engineer", "canonical_role_id": "welding_engineer", "is_active": True},
    {"alias": "Corrosion Prevention Engineer", "canonical_role_id": "corrosion_engineer", "is_active": True},
    {"alias": "Polymer Materials Engineer", "canonical_role_id": "polymer_engineer", "is_active": True},
    {"alias": "Composite Materials Engineer", "canonical_role_id": "composites_engineer", "is_active": True},
    {"alias": "Materials Research and Development Engineer", "canonical_role_id": "materials_research_engineer", "is_active": True},
    {"alias": "Metallurgical Production Process Engineer", "canonical_role_id": "metallurgical_process_engineer", "is_active": True},
    {"alias": "Head of Materials Engineering", "canonical_role_id": "materials_engineering_manager", "is_active": True},

    # --------------------------------------------------------
    # 9. Quality, Testing & Reliability Engineering
    # --------------------------------------------------------
    {"alias": "Product Quality Engineer", "canonical_role_id": "quality_engineer", "is_active": True},
    {"alias": "Quality Assurance (QA) Engineer", "canonical_role_id": "quality_assurance_engineer", "is_active": True},
    {"alias": "Quality Control (QC) Engineer", "canonical_role_id": "quality_control_engineer", "is_active": True},
    {"alias": "Product Reliability Engineer", "canonical_role_id": "reliability_engineer", "is_active": True},
    {"alias": "Engineering Test Engineer", "canonical_role_id": "test_engineer", "is_active": True},
    {"alias": "Product Validation Engineer", "canonical_role_id": "validation_engineer", "is_active": True},
    {"alias": "Quality Management Systems Engineer", "canonical_role_id": "quality_systems_engineer", "is_active": True},
    {"alias": "Supplier Development Quality Engineer", "canonical_role_id": "supplier_quality_engineer", "is_active": True},
    {"alias": "Quality Inspection Specialist", "canonical_role_id": "quality_inspection_engineer", "is_active": True},
    {"alias": "Head of Quality", "canonical_role_id": "quality_manager", "is_active": True},

    # --------------------------------------------------------
    # 10. Engineering Design & Project Execution
    # --------------------------------------------------------
    {"alias": "Engineering Project Design Specialist", "canonical_role_id": "engineering_project_engineer", "is_active": True},
    {"alias": "Engineering Program Project Manager", "canonical_role_id": "engineering_project_manager", "is_active": True},
    {"alias": "Head of Engineering Design", "canonical_role_id": "engineering_design_manager", "is_active": True},
    {"alias": "Engineering Project Planning Engineer", "canonical_role_id": "project_planning_engineer", "is_active": True},
    {"alias": "Project Cost and Controls Engineer", "canonical_role_id": "project_controls_engineer", "is_active": True},
    {"alias": "Engineering Project Coordinator", "canonical_role_id": "engineering_coordinator", "is_active": True},
    {"alias": "Technical Program Project Manager", "canonical_role_id": "technical_project_manager", "is_active": True},
    {"alias": "Engineering Advisory Consultant", "canonical_role_id": "engineering_consultant", "is_active": True},
    {"alias": "Lead Engineering Designer", "canonical_role_id": "engineering_design_lead", "is_active": True},
    {"alias": "Engineering Program Lead", "canonical_role_id": "engineering_program_manager", "is_active": True},

])


# ============================================================
# ROLE ALIASES — FINANCE & ACCOUNTING
# ============================================================

ROLE_ALIASES.extend([

    # --------------------------------------------------------
    # 1. Accounting & Bookkeeping
    # --------------------------------------------------------
    {"alias": "Senior Accounts Executive", "canonical_role_id": "senior_accountant", "is_active": True},
    {"alias": "Assistant Accountant", "canonical_role_id": "junior_accountant", "is_active": True},
    {"alias": "Accounts Officer", "canonical_role_id": "accounts_executive", "is_active": True},
    {"alias": "Accounts Payable (AP) Analyst", "canonical_role_id": "accounts_payable_specialist", "is_active": True},
    {"alias": "Accounts Receivable (AR) Analyst", "canonical_role_id": "accounts_receivable_specialist", "is_active": True},
    {"alias": "Accounting Bookkeeper", "canonical_role_id": "bookkeeper", "is_active": True},
    {"alias": "GL Accountant", "canonical_role_id": "general_ledger_accountant", "is_active": True},
    {"alias": "Management Cost Accountant", "canonical_role_id": "cost_accountant", "is_active": True},
    {"alias": "Head of Accounting", "canonical_role_id": "accounting_manager", "is_active": True},

    # --------------------------------------------------------
    # 2. Audit & Assurance
    # --------------------------------------------------------
    {"alias": "Internal Audit Specialist", "canonical_role_id": "internal_auditor", "is_active": True},
    {"alias": "Independent External Auditor", "canonical_role_id": "external_auditor", "is_active": True},
    {"alias": "Audit Trainee", "canonical_role_id": "audit_associate", "is_active": True},
    {"alias": "Senior Audit Associate", "canonical_role_id": "audit_senior", "is_active": True},
    {"alias": "Audit Team Manager", "canonical_role_id": "audit_manager", "is_active": True},
    {"alias": "Forensic Accounting Specialist", "canonical_role_id": "forensic_accountant", "is_active": True},
    {"alias": "Information Technology Auditor", "canonical_role_id": "it_auditor", "is_active": True},
    {"alias": "Regulatory Compliance Auditor", "canonical_role_id": "compliance_auditor", "is_active": True},
    {"alias": "Audit and Assurance Analyst", "canonical_role_id": "audit_analyst", "is_active": True},
    {"alias": "Internal Audit Director", "canonical_role_id": "head_of_internal_audit", "is_active": True},

    # --------------------------------------------------------
    # 3. Taxation
    # --------------------------------------------------------
    {"alias": "Corporate Tax Accountant", "canonical_role_id": "tax_accountant", "is_active": True},
    {"alias": "Taxation Analyst", "canonical_role_id": "tax_analyst", "is_active": True},
    {"alias": "Tax Advisory Consultant", "canonical_role_id": "tax_consultant", "is_active": True},
    {"alias": "Head of Tax", "canonical_role_id": "tax_manager", "is_active": True},
    {"alias": "Corporate Tax Analyst", "canonical_role_id": "corporate_tax_specialist", "is_active": True},
    {"alias": "Global Tax Specialist", "canonical_role_id": "international_tax_specialist", "is_active": True},
    {"alias": "Goods and Services Tax (GST) Specialist", "canonical_role_id": "gst_specialist", "is_active": True},
    {"alias": "Transfer Pricing Specialist", "canonical_role_id": "transfer_pricing_analyst", "is_active": True},
    {"alias": "Tax Compliance Analyst", "canonical_role_id": "tax_compliance_specialist", "is_active": True},
    {"alias": "Head of Taxation", "canonical_role_id": "tax_director", "is_active": True},

    # --------------------------------------------------------
    # 4. Financial Management & Controlling
    # --------------------------------------------------------
    {"alias": "Head of Finance", "canonical_role_id": "finance_manager", "is_active": True},
    {"alias": "Financial Controls Analyst", "canonical_role_id": "financial_control_analyst", "is_active": True},
    {"alias": "Finance and Business Partner", "canonical_role_id": "finance_business_partner", "is_active": True},
    {"alias": "Treasury Finance Analyst", "canonical_role_id": "treasury_analyst", "is_active": True},
    {"alias": "Head of Treasury", "canonical_role_id": "treasury_manager", "is_active": True},
    {"alias": "Financial Statements Reporting Manager", "canonical_role_id": "financial_reporting_manager", "is_active": True},
    {"alias": "Finance Operations Manager", "canonical_role_id": "financial_operations_manager", "is_active": True},
    {"alias": "CFO", "canonical_role_id": "chief_financial_officer", "is_active": True},

    # --------------------------------------------------------
    # 5. Financial Planning & Analysis
    # --------------------------------------------------------
    {"alias": "Financial Planning and Analysis Analyst", "canonical_role_id": "financial_planning_analyst", "is_active": True},
    {"alias": "Financial Planning and Analysis (FP&A) Analyst", "canonical_role_id": "fp_and_a_analyst", "is_active": True},
    {"alias": "Senior Financial Planning and Analysis Analyst", "canonical_role_id": "senior_fp_and_a_analyst", "is_active": True},
    {"alias": "Financial Planning and Analysis Manager", "canonical_role_id": "financial_planning_manager", "is_active": True},
    {"alias": "FP&A Lead", "canonical_role_id": "fp_and_a_manager", "is_active": True},
    {"alias": "Financial Budget Analyst", "canonical_role_id": "budget_analyst", "is_active": True},
    {"alias": "Financial Forecast Analyst", "canonical_role_id": "forecasting_analyst", "is_active": True},
    {"alias": "Financial Modeling Specialist", "canonical_role_id": "financial_modeling_analyst", "is_active": True},
    {"alias": "Corporate Finance Specialist", "canonical_role_id": "corporate_finance_analyst", "is_active": True},
    {"alias": "Head of Financial Planning and Analysis", "canonical_role_id": "director_of_fp_and_a", "is_active": True},

    # --------------------------------------------------------
    # 6. Banking & Credit
    # --------------------------------------------------------
    {"alias": "Banking Operations Associate", "canonical_role_id": "banking_associate", "is_active": True},
    {"alias": "Bank Relationship Manager", "canonical_role_id": "relationship_manager_banking", "is_active": True},
    {"alias": "Credit Risk Assessment Analyst", "canonical_role_id": "credit_analyst", "is_active": True},
    {"alias": "Head of Credit", "canonical_role_id": "credit_manager", "is_active": True},
    {"alias": "Loan Executive", "canonical_role_id": "loan_officer", "is_active": True},
    {"alias": "Bank Operations Analyst", "canonical_role_id": "banking_operations_analyst", "is_active": True},
    {"alias": "Bank Branch Head", "canonical_role_id": "branch_manager_banking", "is_active": True},
    {"alias": "Credit Risk Management Analyst", "canonical_role_id": "credit_risk_analyst", "is_active": True},
    {"alias": "Trade Finance Analyst", "canonical_role_id": "trade_finance_specialist", "is_active": True},
    {"alias": "Head of Banking", "canonical_role_id": "banking_manager", "is_active": True},

    # --------------------------------------------------------
    # 7. Investment & Asset Management
    # --------------------------------------------------------
    {"alias": "Investment Research Analyst", "canonical_role_id": "investment_analyst", "is_active": True},
    {"alias": "Equity Research Associate", "canonical_role_id": "equity_research_analyst", "is_active": True},
    {"alias": "Investment Portfolio Manager", "canonical_role_id": "portfolio_manager", "is_active": True},
    {"alias": "Asset Management Specialist", "canonical_role_id": "asset_manager", "is_active": True},
    {"alias": "Investment Banking Associate", "canonical_role_id": "investment_banker", "is_active": True},
    {"alias": "Investment Fund Manager", "canonical_role_id": "fund_manager", "is_active": True},
    {"alias": "Private Wealth Manager", "canonical_role_id": "wealth_manager", "is_active": True},
    {"alias": "Investment Operations Specialist", "canonical_role_id": "investment_operations_analyst", "is_active": True},
    {"alias": "Private Equity Research Analyst", "canonical_role_id": "private_equity_analyst", "is_active": True},
    {"alias": "Head of Investment Management", "canonical_role_id": "investment_management_director", "is_active": True},

    # --------------------------------------------------------
    # 8. Insurance & Risk Management
    # --------------------------------------------------------
    {"alias": "Insurance Business Analyst", "canonical_role_id": "insurance_analyst", "is_active": True},
    {"alias": "Insurance Risk Underwriter", "canonical_role_id": "insurance_underwriter", "is_active": True},
    {"alias": "Insurance Claims Analyst", "canonical_role_id": "insurance_claims_analyst", "is_active": True},
    {"alias": "Insurance Claims Adjuster", "canonical_role_id": "claims_adjuster", "is_active": True},
    {"alias": "Actuarial Analyst", "canonical_role_id": "actuary", "is_active": True},
    {"alias": "Enterprise Risk Analyst", "canonical_role_id": "risk_analyst", "is_active": True},
    {"alias": "Head of Insurance", "canonical_role_id": "insurance_manager", "is_active": True},
    {"alias": "Enterprise Risk Management Director", "canonical_role_id": "enterprise_risk_manager", "is_active": True},
    {"alias": "Insurance Sales Broker", "canonical_role_id": "insurance_broker", "is_active": True},

])


# ============================================================
# ROLE ALIASES — SALES & BUSINESS DEVELOPMENT
# ============================================================

ROLE_ALIASES.extend([

    # --------------------------------------------------------
    # 1. Business Development & Partnerships
    # --------------------------------------------------------
    {"alias": "Business Development Officer", "canonical_role_id": "business_development_executive", "is_active": True},
    {"alias": "Business Development Lead", "canonical_role_id": "business_development_manager", "is_active": True},
    {"alias": "Business Development Representative", "canonical_role_id": "business_development_associate", "is_active": True},
    {"alias": "Partnership Development Manager", "canonical_role_id": "partnerships_manager", "is_active": True},
    {"alias": "Strategic Alliance Manager", "canonical_role_id": "strategic_partnerships_manager", "is_active": True},
    {"alias": "Head of Business Development", "canonical_role_id": "business_development_director", "is_active": True},
    {"alias": "Channel Partner Manager", "canonical_role_id": "channel_partnerships_manager", "is_active": True},
    {"alias": "Corporate Development Lead", "canonical_role_id": "corporate_development_manager", "is_active": True},
    {"alias": "Business Expansion Manager", "canonical_role_id": "business_growth_manager", "is_active": True},

    # --------------------------------------------------------
    # 2. Inside & Field Sales
    # --------------------------------------------------------
    {"alias": "Sales Officer", "canonical_role_id": "sales_executive", "is_active": True},
    {"alias": "Inside Sales Officer", "canonical_role_id": "inside_sales_executive", "is_active": True},
    {"alias": "Inside Sales Agent", "canonical_role_id": "inside_sales_representative", "is_active": True},
    {"alias": "Field Sales Officer", "canonical_role_id": "field_sales_executive", "is_active": True},
    {"alias": "Field Sales Team Manager", "canonical_role_id": "field_sales_manager", "is_active": True},
    {"alias": "Sales Agent", "canonical_role_id": "sales_representative", "is_active": True},
    {"alias": "Territory Business Manager", "canonical_role_id": "territory_sales_manager", "is_active": True},
    {"alias": "Regional Sales Head", "canonical_role_id": "regional_sales_manager", "is_active": True},
    {"alias": "Head of Sales", "canonical_role_id": "sales_manager", "is_active": True},
    {"alias": "VP of Sales", "canonical_role_id": "sales_director", "is_active": True},

    # --------------------------------------------------------
    # 3. Enterprise & B2B Sales
    # --------------------------------------------------------
    {"alias": "Business-to-Business Sales Executive", "canonical_role_id": "b2b_sales_executive", "is_active": True},
    {"alias": "Enterprise Account Executive", "canonical_role_id": "enterprise_sales_executive", "is_active": True},
    {"alias": "Enterprise Sales Lead", "canonical_role_id": "enterprise_sales_manager", "is_active": True},
    {"alias": "Key Account Sales Lead", "canonical_role_id": "key_account_sales_manager", "is_active": True},
    {"alias": "Strategic Account Sales Executive", "canonical_role_id": "strategic_account_executive", "is_active": True},
    {"alias": "Corporate Account Sales Manager", "canonical_role_id": "corporate_sales_manager", "is_active": True},
    {"alias": "Head of National Sales", "canonical_role_id": "national_sales_manager", "is_active": True},
    {"alias": "Global Strategic Account Manager", "canonical_role_id": "global_account_manager", "is_active": True},
    {"alias": "Head of B2B Sales", "canonical_role_id": "b2b_sales_director", "is_active": True},

    # --------------------------------------------------------
    # 4. Account Management & Client Relations
    # --------------------------------------------------------
    {"alias": "Client Account Manager", "canonical_role_id": "account_manager", "is_active": True},
    {"alias": "Strategic Key Account Manager", "canonical_role_id": "key_account_manager", "is_active": True},
    {"alias": "Customer Relationship Manager", "canonical_role_id": "client_relationship_manager", "is_active": True},
    {"alias": "Client Account Representative", "canonical_role_id": "client_account_executive", "is_active": True},
    {"alias": "Strategic Client Account Manager", "canonical_role_id": "strategic_account_manager", "is_active": True},
    {"alias": "Client Account Director", "canonical_role_id": "account_director", "is_active": True},
    {"alias": "Client Services Team Manager", "canonical_role_id": "client_services_manager", "is_active": True},
    {"alias": "Head of Account Management", "canonical_role_id": "account_management_director", "is_active": True},

    # --------------------------------------------------------
    # 5. Sales Operations & Enablement
    # --------------------------------------------------------
    {"alias": "Sales Operations Specialist", "canonical_role_id": "sales_operations_analyst", "is_active": True},
    {"alias": "Head of Sales Operations", "canonical_role_id": "sales_operations_manager", "is_active": True},
    {"alias": "Sales Training and Enablement Manager", "canonical_role_id": "sales_enablement_manager", "is_active": True},
    {"alias": "Sales Enablement Coordinator", "canonical_role_id": "sales_enablement_specialist", "is_active": True},
    {"alias": "Sales Performance Analyst", "canonical_role_id": "sales_analyst", "is_active": True},
    {"alias": "Salesforce CRM Administrator", "canonical_role_id": "salesforce_administrator", "is_active": True},
    {"alias": "Sales Incentive Compensation Analyst", "canonical_role_id": "sales_compensation_analyst", "is_active": True},
    {"alias": "Sales Planning and Strategy Manager", "canonical_role_id": "sales_strategy_manager", "is_active": True},
    {"alias": "RevOps Manager", "canonical_role_id": "revenue_operations_manager", "is_active": True},

    # --------------------------------------------------------
    # 6. Channel & Retail Sales
    # --------------------------------------------------------
    {"alias": "Channel Sales Officer", "canonical_role_id": "channel_sales_executive", "is_active": True},
    {"alias": "Head of Channel Sales", "canonical_role_id": "channel_sales_manager", "is_active": True},
    {"alias": "Retail Sales Associate", "canonical_role_id": "retail_sales_executive", "is_active": True},
    {"alias": "Retail Sales Head", "canonical_role_id": "retail_sales_manager", "is_active": True},
    {"alias": "Distributor Relationship Manager", "canonical_role_id": "distributor_sales_manager", "is_active": True},
    {"alias": "Channel Partner Account Manager", "canonical_role_id": "channel_account_manager", "is_active": True},
    {"alias": "Channel Partner Development Manager", "canonical_role_id": "channel_development_manager", "is_active": True},
    {"alias": "Retail Sales Floor Supervisor", "canonical_role_id": "retail_store_sales_supervisor", "is_active": True},
    {"alias": "Regional Head of Channel Sales", "canonical_role_id": "regional_channel_manager", "is_active": True},

    # --------------------------------------------------------
    # 7. Pre-Sales & Solutions Consulting
    # --------------------------------------------------------
    {"alias": "Pre-Sales Specialist", "canonical_role_id": "presales_consultant", "is_active": True},
    {"alias": "Business Solutions Consultant", "canonical_role_id": "solutions_consultant", "is_active": True},
    {"alias": "Technical Solutions Engineer", "canonical_role_id": "solutions_engineer", "is_active": True},
    {"alias": "Technical Sales Engineer", "canonical_role_id": "sales_engineer", "is_active": True},
    {"alias": "Pre-Sales Solutions Engineer", "canonical_role_id": "technical_presales_engineer", "is_active": True},
    {"alias": "Head of Pre-Sales", "canonical_role_id": "presales_manager", "is_active": True},
    {"alias": "Pre-Sales Technical Architect", "canonical_role_id": "solutions_architect_presales", "is_active": True},
    {"alias": "Sales Advisory Manager", "canonical_role_id": "sales_consulting_manager", "is_active": True},

])


# ============================================================
# MARKETING & COMMUNICATIONS — ROLE ALIASES
# ============================================================

ROLE_ALIASES.extend([

    # Digital & Performance Marketing
    {"alias": "Digital Marketing Specialist", "canonical_role_id": "digital_marketing_executive"},
    {"alias": "Online Marketing Executive", "canonical_role_id": "digital_marketing_executive"},
    {"alias": "Digital Marketing Lead", "canonical_role_id": "digital_marketing_manager"},
    {"alias": "Online Marketing Manager", "canonical_role_id": "digital_marketing_manager"},
    {"alias": "Performance Marketing Lead", "canonical_role_id": "performance_marketing_manager"},
    {"alias": "Paid Advertising Manager", "canonical_role_id": "performance_marketing_manager"},
    {"alias": "Performance Marketing Executive", "canonical_role_id": "performance_marketing_specialist"},
    {"alias": "Paid Campaign Specialist", "canonical_role_id": "performance_marketing_specialist"},
    {"alias": "SEO Analyst", "canonical_role_id": "seo_specialist"},
    {"alias": "Search Engine Optimization Specialist", "canonical_role_id": "seo_specialist"},
    {"alias": "Search Engine Optimization Manager", "canonical_role_id": "seo_manager"},
    {"alias": "Search Marketing Manager", "canonical_role_id": "seo_manager"},
    {"alias": "Search Engine Marketing Executive", "canonical_role_id": "sem_specialist"},
    {"alias": "Search Advertising Specialist", "canonical_role_id": "sem_specialist"},
    {"alias": "Digital Advertising Specialist", "canonical_role_id": "paid_media_specialist"},
    {"alias": "Paid Search Specialist", "canonical_role_id": "paid_media_specialist"},
    {"alias": "Social Media Manager", "canonical_role_id": "social_media_marketing_manager"},
    {"alias": "Social Media Marketing Lead", "canonical_role_id": "social_media_marketing_manager"},
    {"alias": "Online Campaign Manager", "canonical_role_id": "digital_campaign_manager"},
    {"alias": "Digital Advertising Campaign Manager", "canonical_role_id": "digital_campaign_manager"},

    # Brand & Product Marketing
    {"alias": "Assistant Brand Manager", "canonical_role_id": "assistant_brand_manager"},
    {"alias": "Brand Marketing Lead", "canonical_role_id": "brand_marketing_manager"},
    {"alias": "Product Marketing Lead", "canonical_role_id": "product_marketing_manager"},
    {"alias": "Product Marketing Executive", "canonical_role_id": "product_marketing_specialist"},
    {"alias": "Go To Market Manager", "canonical_role_id": "go_to_market_manager"},
    {"alias": "GTM Manager", "canonical_role_id": "go_to_market_manager"},
    {"alias": "Brand Planning Manager", "canonical_role_id": "brand_strategy_manager"},
    {"alias": "Brand Strategist", "canonical_role_id": "brand_strategy_manager"},
    {"alias": "New Product Launch Manager", "canonical_role_id": "product_launch_manager"},
    {"alias": "Product Introduction Manager", "canonical_role_id": "product_launch_manager"},
    {"alias": "Head of Brand", "canonical_role_id": "brand_director"},

    # Content, Copywriting & Communications
    {"alias": "Web Content Writer", "canonical_role_id": "content_writer"},
    {"alias": "Digital Content Writer", "canonical_role_id": "content_writer"},
    {"alias": "Content Marketing Lead", "canonical_role_id": "content_marketing_manager"},
    {"alias": "Content Marketing Director", "canonical_role_id": "content_marketing_manager"},
    {"alias": "Editorial Content Strategist", "canonical_role_id": "content_strategist"},
    {"alias": "Content Strategy Lead", "canonical_role_id": "content_strategist"},
    {"alias": "Advertising Copywriter", "canonical_role_id": "copywriter"},
    {"alias": "Creative Copywriter", "canonical_role_id": "copywriter"},
    {"alias": "Lead Copywriter", "canonical_role_id": "senior_copywriter"},
    {"alias": "Managing Content Editor", "canonical_role_id": "content_editor"},
    {"alias": "Web Content Manager", "canonical_role_id": "content_manager"},
    {"alias": "Digital Content Manager", "canonical_role_id": "content_manager"},
    {"alias": "Corporate Communications Specialist", "canonical_role_id": "communications_specialist"},
    {"alias": "Content Editorial Director", "canonical_role_id": "content_director"},

    # Public Relations & Corporate Communications
    {"alias": "PR Specialist", "canonical_role_id": "public_relations_specialist"},
    {"alias": "PR Executive", "canonical_role_id": "public_relations_specialist"},
    {"alias": "PR Manager", "canonical_role_id": "public_relations_manager"},
    {"alias": "Corporate Communications Lead", "canonical_role_id": "corporate_communications_manager"},
    {"alias": "Corporate Communication Manager", "canonical_role_id": "corporate_communications_manager"},
    {"alias": "Corporate Communications Director", "canonical_role_id": "corporate_communications_manager"},
    {"alias": "Communications Lead", "canonical_role_id": "communications_manager"},
    {"alias": "Media Relations Specialist", "canonical_role_id": "media_relations_manager"},
    {"alias": "Press Relations Manager", "canonical_role_id": "media_relations_manager"},
    {"alias": "Publicity Executive", "canonical_role_id": "publicity_manager"},
    {"alias": "Press Officer", "canonical_role_id": "publicity_manager"},
    {"alias": "Employee Communications Manager", "canonical_role_id": "internal_communications_manager"},
    {"alias": "Internal Communications Specialist", "canonical_role_id": "internal_communications_manager"},
    {"alias": "Government and Corporate Affairs Manager", "canonical_role_id": "corporate_affairs_manager"},
    {"alias": "PR Director", "canonical_role_id": "public_relations_director"},

    # Market Research & Consumer Insights
    {"alias": "Market Research Executive", "canonical_role_id": "market_research_analyst"},
    {"alias": "Marketing Research Analyst", "canonical_role_id": "market_research_analyst"},
    {"alias": "Market Research Lead", "canonical_role_id": "market_research_manager"},
    {"alias": "Consumer Insights Specialist", "canonical_role_id": "consumer_insights_analyst"},
    {"alias": "Consumer Research Analyst", "canonical_role_id": "consumer_insights_analyst"},
    {"alias": "Consumer Insights Lead", "canonical_role_id": "consumer_insights_manager"},
    {"alias": "Market Intelligence Specialist", "canonical_role_id": "market_intelligence_analyst"},
    {"alias": "Competitive Intelligence Specialist", "canonical_role_id": "competitive_intelligence_analyst"},
    {"alias": "Customer Research Specialist", "canonical_role_id": "customer_research_analyst"},
    {"alias": "Head of Market Research", "canonical_role_id": "market_research_director"},

    # Marketing Strategy & Operations
    {"alias": "Marketing Lead", "canonical_role_id": "marketing_manager"},
    {"alias": "Head of Marketing", "canonical_role_id": "marketing_director"},
    {"alias": "Marketing Planning Manager", "canonical_role_id": "marketing_strategy_manager"},
    {"alias": "Marketing Strategy Lead", "canonical_role_id": "marketing_strategy_manager"},
    {"alias": "Marketing Operations Lead", "canonical_role_id": "marketing_operations_manager"},
    {"alias": "Marketing Operations Executive", "canonical_role_id": "marketing_operations_specialist"},
    {"alias": "Marketing Automation Specialist", "canonical_role_id": "marketing_automation_manager"},
    {"alias": "Marketing Automation Lead", "canonical_role_id": "marketing_automation_manager"},
    {"alias": "CMO", "canonical_role_id": "chief_marketing_officer"},
])


# ============================================================
# HUMAN RESOURCES — ROLE ALIASES
# ============================================================

ROLE_ALIASES.extend([

    # Talent Acquisition & Recruitment
    {"alias": "Talent Acquisition Executive", "canonical_role_id": "talent_acquisition_specialist"},
    {"alias": "Recruitment Specialist", "canonical_role_id": "talent_acquisition_specialist"},
    {"alias": "Talent Acquisition Lead", "canonical_role_id": "talent_acquisition_manager"},
    {"alias": "Talent Acquisition Team Lead", "canonical_role_id": "talent_acquisition_manager"},
    {"alias": "IT Recruiter", "canonical_role_id": "technical_recruiter"},
    {"alias": "Technology Recruiter", "canonical_role_id": "technical_recruiter"},
    {"alias": "Senior Executive Recruiter", "canonical_role_id": "executive_recruiter"},
    {"alias": "Leadership Recruiter", "canonical_role_id": "executive_recruiter"},
    {"alias": "Recruitment Administrator", "canonical_role_id": "recruitment_coordinator"},
    {"alias": "Talent Acquisition Coordinator", "canonical_role_id": "recruitment_coordinator"},
    {"alias": "Talent Sourcer", "canonical_role_id": "sourcing_specialist"},
    {"alias": "Recruitment Sourcer", "canonical_role_id": "sourcing_specialist"},
    {"alias": "Talent Acquisition Operations Manager", "canonical_role_id": "recruitment_manager"},
    {"alias": "Recruitment Team Manager", "canonical_role_id": "recruitment_manager"},
    {"alias": "Talent Acquisition Director", "canonical_role_id": "head_of_talent_acquisition"},
    {"alias": "Director of Talent Acquisition", "canonical_role_id": "head_of_talent_acquisition"},

    # HR Operations & Administration
    {"alias": "Human Resources Executive", "canonical_role_id": "hr_executive"},
    {"alias": "Human Resources Generalist", "canonical_role_id": "hr_generalist"},
    {"alias": "HR Lead", "canonical_role_id": "hr_manager"},
    {"alias": "Human Resources Manager", "canonical_role_id": "hr_manager"},
    {"alias": "HR Operations Executive", "canonical_role_id": "hr_operations_specialist"},
    {"alias": "Human Resources Operations Specialist", "canonical_role_id": "hr_operations_specialist"},
    {"alias": "Human Resources Administrator", "canonical_role_id": "hr_administrator"},
    {"alias": "Human Resources Coordinator", "canonical_role_id": "hr_coordinator"},
    {"alias": "HR Team Coordinator", "canonical_role_id": "hr_coordinator"},
    {"alias": "Head of Human Resources", "canonical_role_id": "hr_director"},
    {"alias": "Director of Human Resources", "canonical_role_id": "hr_director"},

    # Learning & Development
    {"alias": "L&D Specialist", "canonical_role_id": "learning_development_specialist"},
    {"alias": "Learning and Development Executive", "canonical_role_id": "learning_development_specialist"},
    {"alias": "L&D Manager", "canonical_role_id": "learning_development_manager"},
    {"alias": "Learning and Development Lead", "canonical_role_id": "learning_development_manager"},
    {"alias": "Corporate Training Manager", "canonical_role_id": "training_manager"},
    {"alias": "Training and Development Manager", "canonical_role_id": "training_manager"},
    {"alias": "Training Executive", "canonical_role_id": "training_coordinator"},
    {"alias": "Learning and Development Consultant", "canonical_role_id": "learning_consultant"},
    {"alias": "Organizational Development Consultant", "canonical_role_id": "organizational_development_specialist"},
    {"alias": "OD Specialist", "canonical_role_id": "organizational_development_specialist"},
    {"alias": "Leadership Training Manager", "canonical_role_id": "leadership_development_manager"},
    {"alias": "Leadership Development Lead", "canonical_role_id": "leadership_development_manager"},
    {"alias": "Head of Learning and Development", "canonical_role_id": "learning_development_director"},

    # Compensation, Benefits & Payroll
    {"alias": "C&B Specialist", "canonical_role_id": "compensation_benefits_specialist"},
    {"alias": "Total Rewards Specialist", "canonical_role_id": "compensation_benefits_specialist"},
    {"alias": "Compensation and Rewards Analyst", "canonical_role_id": "compensation_analyst"},
    {"alias": "Salary Analyst", "canonical_role_id": "compensation_analyst"},
    {"alias": "Compensation and Benefits Lead", "canonical_role_id": "compensation_manager"},
    {"alias": "Total Rewards Manager", "canonical_role_id": "compensation_manager"},
    {"alias": "Employee Benefits Administrator", "canonical_role_id": "benefits_administrator"},
    {"alias": "Benefits Specialist", "canonical_role_id": "benefits_administrator"},
    {"alias": "Employee Benefits Manager", "canonical_role_id": "benefits_manager"},
    {"alias": "Payroll Executive", "canonical_role_id": "payroll_specialist"},
    {"alias": "Payroll Administrator", "canonical_role_id": "payroll_specialist"},
    {"alias": "Payroll Team Lead", "canonical_role_id": "payroll_manager"},
    {"alias": "Head of Payroll", "canonical_role_id": "payroll_manager"},
    {"alias": "Total Rewards and Benefits Manager", "canonical_role_id": "compensation_benefits_manager"},
    {"alias": "C&B Manager", "canonical_role_id": "compensation_benefits_manager"},

    # Employee Relations & Engagement
    {"alias": "Employee Relations Executive", "canonical_role_id": "employee_relations_specialist"},
    {"alias": "Employee Relations Lead", "canonical_role_id": "employee_relations_manager"},
    {"alias": "Workplace Relations Manager", "canonical_role_id": "employee_relations_manager"},
    {"alias": "Employee Engagement Executive", "canonical_role_id": "employee_engagement_specialist"},
    {"alias": "Employee Engagement Lead", "canonical_role_id": "employee_engagement_manager"},
    {"alias": "Workplace Engagement Manager", "canonical_role_id": "employee_engagement_manager"},
    {"alias": "Employee Experience Executive", "canonical_role_id": "employee_experience_specialist"},
    {"alias": "Workforce Experience Specialist", "canonical_role_id": "employee_experience_specialist"},
    {"alias": "Labour Relations Manager", "canonical_role_id": "industrial_relations_manager"},
    {"alias": "Labor Relations Manager", "canonical_role_id": "industrial_relations_manager"},
    {"alias": "Employee Experience Lead", "canonical_role_id": "employee_experience_manager"},
    {"alias": "Head of Employee Relations", "canonical_role_id": "employee_relations_director"},

    # HR Strategy & Business Partnering
    {"alias": "Human Resources Business Partner", "canonical_role_id": "hr_business_partner"},
    {"alias": "HRBP", "canonical_role_id": "hr_business_partner"},
    {"alias": "Senior Human Resources Business Partner", "canonical_role_id": "senior_hr_business_partner"},
    {"alias": "Senior HRBP", "canonical_role_id": "senior_hr_business_partner"},
    {"alias": "People Strategy Lead", "canonical_role_id": "hr_strategy_manager"},
    {"alias": "Human Resources Strategy Manager", "canonical_role_id": "hr_strategy_manager"},
    {"alias": "People and Culture Strategy Manager", "canonical_role_id": "people_strategy_manager"},
    {"alias": "Workforce Planning Lead", "canonical_role_id": "workforce_planning_manager"},
    {"alias": "Strategic Workforce Planning Manager", "canonical_role_id": "workforce_planning_manager"},
    {"alias": "Organizational Development Lead", "canonical_role_id": "organizational_development_manager"},
    {"alias": "OD Manager", "canonical_role_id": "organizational_development_manager"},
    {"alias": "CHRO", "canonical_role_id": "chief_human_resources_officer"},
    {"alias": "Chief People Officer", "canonical_role_id": "chief_human_resources_officer"},
    {"alias": "VP Human Resources", "canonical_role_id": "vice_president_human_resources"},
    {"alias": "VP of HR", "canonical_role_id": "vice_president_human_resources"},
])


# ============================================================
# OPERATIONS & ADMINISTRATION — ROLE ALIASES
# ============================================================

ROLE_ALIASES.extend([

    # Business Operations & Process Management
    {"alias": "Business Operations Lead", "canonical_role_id": "business_operations_manager"},
    {"alias": "Business Operations Team Manager", "canonical_role_id": "business_operations_manager"},
    {"alias": "Operations Lead", "canonical_role_id": "operations_manager"},
    {"alias": "Operational Manager", "canonical_role_id": "operations_manager"},
    {"alias": "Business Operations Executive", "canonical_role_id": "business_operations_analyst"},
    {"alias": "Business Operations Coordinator", "canonical_role_id": "operations_coordinator"},
    {"alias": "Operations Administrator", "canonical_role_id": "operations_coordinator"},
    {"alias": "Director of Business Operations", "canonical_role_id": "business_operations_director"},
    {"alias": "Business Operations Head", "canonical_role_id": "business_operations_director"},
    {"alias": "Operations Administrator Executive", "canonical_role_id": "operations_executive"},
    {"alias": "Operations Associate", "canonical_role_id": "operations_executive"},
    {"alias": "Business Operations Associate", "canonical_role_id": "business_operations_specialist"},
    {"alias": "Operations Specialist", "canonical_role_id": "business_operations_specialist"},
    {"alias": "Director of Operations", "canonical_role_id": "head_of_operations"},
    {"alias": "Chief Operating Officer", "canonical_role_id": "head_of_operations"},

    # Office Administration & Executive Support
    {"alias": "Administrative Secretary", "canonical_role_id": "administrative_assistant"},
    {"alias": "Admin Assistant", "canonical_role_id": "administrative_assistant"},
    {"alias": "Office Administrator Executive", "canonical_role_id": "office_administrator"},
    {"alias": "Office Administration Specialist", "canonical_role_id": "office_administrator"},
    {"alias": "Office Operations Manager", "canonical_role_id": "office_manager"},
    {"alias": "Administrative Office Manager", "canonical_role_id": "office_manager"},
    {"alias": "Executive Secretary", "canonical_role_id": "executive_assistant"},
    {"alias": "Senior Executive Assistant", "canonical_role_id": "executive_assistant"},
    {"alias": "Private Assistant", "canonical_role_id": "personal_assistant"},
    {"alias": "Private Secretary", "canonical_role_id": "personal_assistant"},
    {"alias": "Head of Administration", "canonical_role_id": "administration_manager"},
    {"alias": "Administrative Services Manager", "canonical_role_id": "administration_manager"},
    {"alias": "Admin Coordinator", "canonical_role_id": "administrative_coordinator"},
    {"alias": "Office Administration Coordinator", "canonical_role_id": "administrative_coordinator"},
    {"alias": "Senior Administrative Officer", "canonical_role_id": "executive_administrator"},
    {"alias": "Executive Office Administrator", "canonical_role_id": "executive_administrator"},

    # Supply Chain, Logistics & Distribution
    {"alias": "Supply Chain Operations Manager", "canonical_role_id": "supply_chain_manager"},
    {"alias": "Head of Supply Chain", "canonical_role_id": "supply_chain_manager"},
    {"alias": "Logistics Operations Manager", "canonical_role_id": "logistics_manager"},
    {"alias": "Head of Logistics", "canonical_role_id": "logistics_manager"},
    {"alias": "Logistics Executive", "canonical_role_id": "logistics_coordinator"},
    {"alias": "Logistics Administrator", "canonical_role_id": "logistics_coordinator"},
    {"alias": "Distribution Operations Manager", "canonical_role_id": "distribution_manager"},
    {"alias": "Head of Distribution", "canonical_role_id": "distribution_manager"},
    {"alias": "Warehouse Operations Manager", "canonical_role_id": "warehouse_manager"},
    {"alias": "Warehouse Operations Head", "canonical_role_id": "warehouse_manager"},
    {"alias": "Stock Controller", "canonical_role_id": "inventory_controller"},
    {"alias": "Inventory Management Specialist", "canonical_role_id": "inventory_controller"},
    {"alias": "Transport Manager", "canonical_role_id": "transportation_manager"},
    {"alias": "Transportation Operations Manager", "canonical_role_id": "transportation_manager"},
    {"alias": "Fleet Operations Manager", "canonical_role_id": "fleet_manager"},
    {"alias": "Fleet Operations Head", "canonical_role_id": "fleet_manager"},

    # Procurement & Purchasing
    {"alias": "Purchasing Specialist", "canonical_role_id": "procurement_specialist"},
    {"alias": "Head of Procurement", "canonical_role_id": "procurement_manager"},
    {"alias": "Procurement Lead", "canonical_role_id": "procurement_manager"},
    {"alias": "Purchasing Lead", "canonical_role_id": "purchasing_manager"},
    {"alias": "Head of Purchasing", "canonical_role_id": "purchasing_manager"},
    {"alias": "Procurement Executive", "canonical_role_id": "procurement_officer"},
    {"alias": "Procurement Administrator", "canonical_role_id": "procurement_officer"},
    {"alias": "Purchasing Agent", "canonical_role_id": "buyer"},
    {"alias": "Purchasing Buyer", "canonical_role_id": "buyer"},
    {"alias": "Strategic Sourcing Lead", "canonical_role_id": "strategic_sourcing_manager"},
    {"alias": "Strategic Procurement Manager", "canonical_role_id": "strategic_sourcing_manager"},
    {"alias": "Supplier Relationship Manager", "canonical_role_id": "vendor_manager"},
    {"alias": "Supplier Manager", "canonical_role_id": "vendor_manager"},
    {"alias": "Director of Procurement", "canonical_role_id": "procurement_director"},
    {"alias": "Chief Procurement Officer", "canonical_role_id": "procurement_director"},

    # Facilities & Workplace Management
    {"alias": "Building Facilities Manager", "canonical_role_id": "facilities_manager"},
    {"alias": "Facilities Operations Lead", "canonical_role_id": "facilities_manager"},
    {"alias": "Facilities Administrator", "canonical_role_id": "facilities_coordinator"},
    {"alias": "Facilities Executive", "canonical_role_id": "facilities_coordinator"},
    {"alias": "Workplace Operations Manager", "canonical_role_id": "workplace_manager"},
    {"alias": "Office Workplace Manager", "canonical_role_id": "workplace_manager"},
    {"alias": "Building Operations Manager", "canonical_role_id": "building_manager"},
    {"alias": "Property Building Manager", "canonical_role_id": "building_manager"},
    {"alias": "Employee Workplace Experience Manager", "canonical_role_id": "workplace_experience_manager"},
    {"alias": "Workplace Experience Lead", "canonical_role_id": "workplace_experience_manager"},
    {"alias": "Facilities and Operations Manager", "canonical_role_id": "facilities_operations_manager"},
    {"alias": "Facilities Services Manager", "canonical_role_id": "facilities_operations_manager"},
    {"alias": "Head of Facilities", "canonical_role_id": "facilities_director"},
    {"alias": "Director of Facilities Management", "canonical_role_id": "facilities_director"},
    {"alias": "Workplace Services Lead", "canonical_role_id": "workplace_services_manager"},
    {"alias": "Workplace Support Services Manager", "canonical_role_id": "workplace_services_manager"},

    # Process Improvement & Business Excellence
    {"alias": "Process Excellence Manager", "canonical_role_id": "process_improvement_manager"},
    {"alias": "Process Optimization Manager", "canonical_role_id": "process_improvement_manager"},
    {"alias": "Business Excellence Lead", "canonical_role_id": "business_excellence_manager"},
    {"alias": "Business Performance Excellence Manager", "canonical_role_id": "business_excellence_manager"},
    {"alias": "Process Improvement Analyst", "canonical_role_id": "process_improvement_specialist"},
    {"alias": "Process Excellence Specialist", "canonical_role_id": "process_improvement_specialist"},
    {"alias": "Operational Excellence Lead", "canonical_role_id": "operational_excellence_manager"},
    {"alias": "OPEX Manager", "canonical_role_id": "operational_excellence_manager"},
    {"alias": "Lean Six Sigma Lead", "canonical_role_id": "lean_six_sigma_manager"},
    {"alias": "Continuous Improvement and Lean Manager", "canonical_role_id": "lean_six_sigma_manager"},
    {"alias": "Business Process Lead", "canonical_role_id": "business_process_manager"},
    {"alias": "Business Process Improvement Manager", "canonical_role_id": "business_process_manager"},
    {"alias": "Business Process Analyst Consultant", "canonical_role_id": "business_process_consultant"},
    {"alias": "Process Management Consultant", "canonical_role_id": "business_process_consultant"},
    {"alias": "Continuous Improvement Lead", "canonical_role_id": "continuous_improvement_manager"},
    {"alias": "Continuous Process Improvement Manager", "canonical_role_id": "continuous_improvement_manager"},
])


# ============================================================
# CUSTOMER SUPPORT & BPO — ROLE ALIASES
# ============================================================

ROLE_ALIASES.extend([

    # Customer Service & Customer Care
    {"alias": "Customer Service Agent", "canonical_role_id": "customer_service_executive"},
    {"alias": "Customer Care Representative", "canonical_role_id": "customer_service_representative"},
    {"alias": "Customer Care Agent", "canonical_role_id": "customer_support_agent"},
    {"alias": "Customer Support Executive", "canonical_role_id": "customer_support_representative"},
    {"alias": "Customer Care Specialist", "canonical_role_id": "customer_care_executive"},
    {"alias": "Customer Service Consultant", "canonical_role_id": "customer_service_advisor"},
    {"alias": "Customer Service Officer", "canonical_role_id": "customer_service_associate"},
    {"alias": "Customer Care Associate", "canonical_role_id": "customer_service_associate"},
    {"alias": "Customer Support Coordinator", "canonical_role_id": "customer_service_coordinator"},
    {"alias": "Customer Care Coordinator", "canonical_role_id": "customer_service_coordinator"},
    {"alias": "Customer Service Team Supervisor", "canonical_role_id": "customer_service_supervisor"},
    {"alias": "Customer Care Manager", "canonical_role_id": "customer_service_manager"},

    # Contact Center & Call Center Operations
    {"alias": "Call Centre Agent", "canonical_role_id": "call_center_agent"},
    {"alias": "Inbound Customer Service Agent", "canonical_role_id": "inbound_call_agent"},
    {"alias": "Inbound Call Centre Agent", "canonical_role_id": "inbound_call_agent"},
    {"alias": "Outbound Customer Service Agent", "canonical_role_id": "outbound_call_agent"},
    {"alias": "Outbound Call Centre Agent", "canonical_role_id": "outbound_call_agent"},
    {"alias": "Contact Centre Executive", "canonical_role_id": "contact_center_executive"},
    {"alias": "Call Center Team Lead", "canonical_role_id": "call_center_team_leader"},
    {"alias": "Call Centre Team Leader", "canonical_role_id": "call_center_team_leader"},
    {"alias": "Call Centre Supervisor", "canonical_role_id": "call_center_supervisor"},
    {"alias": "Contact Centre Manager", "canonical_role_id": "contact_center_manager"},
    {"alias": "Contact Center Operations Manager", "canonical_role_id": "contact_center_manager"},
    {"alias": "Call Centre Manager", "canonical_role_id": "call_center_manager"},
    {"alias": "Call Center Operations Manager", "canonical_role_id": "call_center_manager"},
    {"alias": "Workforce Planning Analyst", "canonical_role_id": "workforce_management_analyst"},
    {"alias": "WFM Analyst", "canonical_role_id": "workforce_management_analyst"},
    {"alias": "Call Center Trainer", "canonical_role_id": "contact_center_trainer"},
    {"alias": "Contact Centre Trainer", "canonical_role_id": "contact_center_trainer"},
    {"alias": "Head of Contact Center", "canonical_role_id": "contact_center_director"},
    {"alias": "Director of Contact Centre Operations", "canonical_role_id": "contact_center_director"},

    # Technical & Product Support
    {"alias": "IT Technical Support Analyst", "canonical_role_id": "technical_support_analyst"},
    {"alias": "Product Support Executive", "canonical_role_id": "product_support_specialist"},
    {"alias": "Product Support Lead", "canonical_role_id": "product_support_manager"},
    {"alias": "Application Support Analyst", "canonical_role_id": "application_support_specialist"},
    {"alias": "Software Support Specialist", "canonical_role_id": "software_support_engineer"},
    {"alias": "Software Technical Support Engineer", "canonical_role_id": "software_support_engineer"},
    {"alias": "Hardware Support Engineer", "canonical_role_id": "hardware_support_specialist"},
    {"alias": "Hardware Support Technician", "canonical_role_id": "hardware_support_specialist"},
    {"alias": "Product Support Executive Analyst", "canonical_role_id": "product_support_analyst"},
    {"alias": "Technical Support Lead", "canonical_role_id": "technical_support_manager"},
    {"alias": "Technical Support Team Manager", "canonical_role_id": "technical_support_manager"},
    {"alias": "Product Support Administrator", "canonical_role_id": "product_support_coordinator"},
    {"alias": "Service Desk Technician", "canonical_role_id": "service_desk_analyst"},
    {"alias": "Helpdesk Manager", "canonical_role_id": "help_desk_manager"},
    {"alias": "Help Desk Operations Manager", "canonical_role_id": "help_desk_manager"},

    # Customer Success & Client Services
    {"alias": "Client Success Manager", "canonical_role_id": "customer_success_manager"},
    {"alias": "Customer Success Executive", "canonical_role_id": "customer_success_specialist"},
    {"alias": "Client Success Specialist", "canonical_role_id": "customer_success_specialist"},
    {"alias": "Head of Customer Success", "canonical_role_id": "customer_success_director"},
    {"alias": "Director of Client Success", "canonical_role_id": "customer_success_director"},
    {"alias": "Client Services Administrator", "canonical_role_id": "client_services_coordinator"},
    {"alias": "Client Services Representative", "canonical_role_id": "client_services_executive"},
    {"alias": "Client Relationship Specialist", "canonical_role_id": "customer_success_relationship_specialist"},
    {"alias": "Customer Relationship Specialist", "canonical_role_id": "customer_success_relationship_specialist"},
    {"alias": "Client Onboarding Specialist", "canonical_role_id": "customer_onboarding_specialist"},
    {"alias": "Customer Retention Specialist", "canonical_role_id": "customer_retention_manager"},
    {"alias": "Customer Loyalty Manager", "canonical_role_id": "customer_retention_manager"},
    {"alias": "Customer Success Associate Executive", "canonical_role_id": "customer_success_associate"},
    {"alias": "Client Implementation Specialist", "canonical_role_id": "implementation_specialist"},
    {"alias": "Customer Implementation Specialist", "canonical_role_id": "implementation_specialist"},
    {"alias": "Client Onboarding Manager", "canonical_role_id": "customer_onboarding_manager"},

    # Back Office & Transaction Processing
    {"alias": "Back Office Executive Assistant", "canonical_role_id": "back_office_executive"},
    {"alias": "Back Office Operations Associate", "canonical_role_id": "back_office_associate"},
    {"alias": "Transaction Processing Executive", "canonical_role_id": "transaction_processing_specialist"},
    {"alias": "Back Office Operations Manager", "canonical_role_id": "back_office_manager"},
    {"alias": "Data Processing Associate", "canonical_role_id": "data_processing_executive"},
    {"alias": "Claims Processing Executive", "canonical_role_id": "claims_processing_specialist"},
    {"alias": "Claims Processor", "canonical_role_id": "claims_processing_specialist"},
    {"alias": "Order Processing Executive", "canonical_role_id": "order_processing_specialist"},
    {"alias": "Order Fulfillment Specialist", "canonical_role_id": "order_processing_specialist"},
    {"alias": "Transaction Operations Manager", "canonical_role_id": "transaction_processing_manager"},
    {"alias": "Data Entry Clerk", "canonical_role_id": "data_entry_operator"},
    {"alias": "Data Entry Specialist", "canonical_role_id": "data_entry_operator"},
    {"alias": "Management Information Systems Executive", "canonical_role_id": "mis_executive"},
    {"alias": "MIS Coordinator", "canonical_role_id": "mis_executive"},
    {"alias": "Billing Specialist", "canonical_role_id": "billing_executive"},
    {"alias": "Billing Coordinator", "canonical_role_id": "billing_executive"},

    # Customer Experience, Quality & Escalations
    {"alias": "Customer Experience Executive", "canonical_role_id": "customer_experience_specialist"},
    {"alias": "CX Specialist", "canonical_role_id": "customer_experience_specialist"},
    {"alias": "Customer Experience Lead", "canonical_role_id": "customer_experience_manager"},
    {"alias": "CX Manager", "canonical_role_id": "customer_experience_manager"},
    {"alias": "Customer Service QA Team Leader", "canonical_role_id": "quality_assurance_team_leader"},
    {"alias": "Customer Support QA Team Leader", "canonical_role_id": "quality_assurance_team_leader"},
    {"alias": "Customer Escalation Executive", "canonical_role_id": "customer_escalation_specialist"},
    {"alias": "Customer Complaint Resolution Specialist", "canonical_role_id": "customer_escalation_specialist"},
    {"alias": "Customer Escalation Lead", "canonical_role_id": "customer_escalations_manager"},
    {"alias": "Customer Complaint Manager", "canonical_role_id": "customer_escalations_manager"},
    {"alias": "Customer Experience Analyst", "canonical_role_id": "customer_experience_analyst"},
    {"alias": "CX Analyst", "canonical_role_id": "customer_experience_analyst"},
    {"alias": "Customer Quality Lead", "canonical_role_id": "customer_quality_manager"},
    {"alias": "Customer Service Quality Manager", "canonical_role_id": "customer_quality_manager"},
    {"alias": "Customer Service QA Analyst", "canonical_role_id": "customer_service_quality_analyst"},
    {"alias": "Customer Support Quality Analyst", "canonical_role_id": "customer_service_quality_analyst"},
    {"alias": "Customer Service Quality Auditor", "canonical_role_id": "quality_auditor"},
    {"alias": "Customer Support Quality Auditor", "canonical_role_id": "quality_auditor"},
    {"alias": "Customer Feedback Specialist", "canonical_role_id": "customer_feedback_analyst"},
    {"alias": "Voice of Customer Analyst", "canonical_role_id": "customer_feedback_analyst"},
])


# ============================================================
# PRODUCT & PROJECT MANAGEMENT — ROLE ALIASES
# ============================================================

ROLE_ALIASES.extend([

    # Product Management
    {"alias": "Product Management Specialist", "canonical_role_id": "product_manager"},
    {"alias": "Product Lead", "canonical_role_id": "product_manager"},
    {"alias": "Lead Product Manager", "canonical_role_id": "senior_product_manager"},
    {"alias": "Principal Product Manager", "canonical_role_id": "senior_product_manager"},
    {"alias": "APM", "canonical_role_id": "associate_product_manager"},
    {"alias": "Product Management Associate", "canonical_role_id": "associate_product_manager"},
    {"alias": "Entry Level Product Manager", "canonical_role_id": "junior_product_manager"},
    {"alias": "Technical Product Lead", "canonical_role_id": "technical_product_manager"},
    {"alias": "IT Product Manager", "canonical_role_id": "technical_product_manager"},
    {"alias": "Online Product Manager", "canonical_role_id": "digital_product_manager"},
    {"alias": "Digital Experience Product Manager", "canonical_role_id": "digital_product_manager"},
    {"alias": "Agile Product Owner", "canonical_role_id": "product_owner"},
    {"alias": "Product Ownership Manager", "canonical_role_id": "product_owner"},
    {"alias": "CPO", "canonical_role_id": "chief_product_officer"},
    {"alias": "Chief Product and Technology Officer", "canonical_role_id": "chief_product_officer"},

    # Project Management
    {"alias": "Project Delivery Manager", "canonical_role_id": "project_manager"},
    {"alias": "Project Management Lead", "canonical_role_id": "project_manager"},
    {"alias": "Lead Project Manager", "canonical_role_id": "senior_project_manager"},
    {"alias": "Principal Project Manager", "canonical_role_id": "senior_project_manager"},
    {"alias": "Project Management Associate", "canonical_role_id": "associate_project_manager"},
    {"alias": "Assistant Project Manager", "canonical_role_id": "associate_project_manager"},
    {"alias": "Entry Level Project Manager", "canonical_role_id": "junior_project_manager"},
    {"alias": "IT Delivery Project Manager", "canonical_role_id": "it_project_manager"},
    {"alias": "Technology Project Manager", "canonical_role_id": "it_project_manager"},
    {"alias": "Corporate Project Manager", "canonical_role_id": "business_project_manager"},
    {"alias": "Business Transformation Project Manager", "canonical_role_id": "business_project_manager"},
    {"alias": "Project Management Coordinator", "canonical_role_id": "project_coordinator"},
    {"alias": "Project Administrator", "canonical_role_id": "project_coordinator"},
    {"alias": "Head of Project Management", "canonical_role_id": "project_director"},
    {"alias": "Director of Projects", "canonical_role_id": "project_director"},

    # Program Management
    {"alias": "Programme Manager", "canonical_role_id": "program_manager"},
    {"alias": "Program Delivery Manager", "canonical_role_id": "program_manager"},
    {"alias": "Senior Programme Manager", "canonical_role_id": "senior_program_manager"},
    {"alias": "Principal Program Manager", "canonical_role_id": "senior_program_manager"},
    {"alias": "Program Management Associate", "canonical_role_id": "associate_program_manager"},
    {"alias": "Assistant Program Manager", "canonical_role_id": "associate_program_manager"},
    {"alias": "Technical Programme Manager", "canonical_role_id": "technical_program_manager"},
    {"alias": "IT Program Manager", "canonical_role_id": "technical_program_manager"},
    {"alias": "Business Programme Manager", "canonical_role_id": "business_program_manager"},
    {"alias": "Enterprise Program Manager", "canonical_role_id": "business_program_manager"},
    {"alias": "Program Management Coordinator", "canonical_role_id": "program_coordinator"},
    {"alias": "Programme Coordinator", "canonical_role_id": "program_coordinator"},
    {"alias": "Director of Programs", "canonical_role_id": "program_director"},
    {"alias": "Programme Director", "canonical_role_id": "program_director"},
    {"alias": "Director of Program Management", "canonical_role_id": "head_of_program_management"},
    {"alias": "Program Management Lead", "canonical_role_id": "head_of_program_management"},

    # Portfolio & PMO Management
    {"alias": "Project Portfolio Lead", "canonical_role_id": "project_portfolio_manager"},
    {"alias": "Portfolio Delivery Manager", "canonical_role_id": "project_portfolio_manager"},
    {"alias": "PMO Office Manager", "canonical_role_id": "portfolio_management_office_manager"},
    {"alias": "Portfolio Management Office Lead", "canonical_role_id": "portfolio_management_office_manager"},
    {"alias": "Project Management Office Manager", "canonical_role_id": "pmo_manager"},
    {"alias": "PMO Lead", "canonical_role_id": "pmo_manager"},
    {"alias": "Project Management Office Analyst", "canonical_role_id": "pmo_analyst"},
    {"alias": "PMO Administrator", "canonical_role_id": "pmo_coordinator"},
    {"alias": "Project Office Coordinator", "canonical_role_id": "pmo_coordinator"},
    {"alias": "Portfolio Analyst", "canonical_role_id": "project_portfolio_analyst"},
    {"alias": "Project Portfolio Management Analyst", "canonical_role_id": "project_portfolio_analyst"},
    {"alias": "Portfolio Controls Manager", "canonical_role_id": "portfolio_governance_manager"},
    {"alias": "Portfolio Oversight Manager", "canonical_role_id": "portfolio_governance_manager"},
    {"alias": "Head of Project Management Office", "canonical_role_id": "head_of_pmo"},
    {"alias": "Director of PMO", "canonical_role_id": "head_of_pmo"},

    # Agile & Scrum Management
    {"alias": "Agile Scrum Master", "canonical_role_id": "scrum_master"},
    {"alias": "Scrum Team Facilitator", "canonical_role_id": "scrum_master"},
    {"alias": "Lead Scrum Master", "canonical_role_id": "senior_scrum_master"},
    {"alias": "Principal Scrum Master", "canonical_role_id": "senior_scrum_master"},
    {"alias": "Agile Transformation Coach", "canonical_role_id": "agile_coach"},
    {"alias": "Agile Methodology Coach", "canonical_role_id": "agile_coach"},
    {"alias": "Enterprise Transformation Coach", "canonical_role_id": "enterprise_agile_coach"},
    {"alias": "Enterprise Scrum Coach", "canonical_role_id": "enterprise_agile_coach"},
    {"alias": "Agile Delivery Lead", "canonical_role_id": "agile_delivery_manager"},
    {"alias": "Agile Program Delivery Manager", "canonical_role_id": "agile_delivery_manager"},
    {"alias": "SAFe Release Train Engineer", "canonical_role_id": "release_train_engineer"},
    {"alias": "Release Train Lead", "canonical_role_id": "release_train_engineer"},
    {"alias": "Agile Project Delivery Manager", "canonical_role_id": "agile_project_manager"},
    {"alias": "Scrum Project Manager", "canonical_role_id": "agile_project_manager"},
    {"alias": "Agile Transformation Lead", "canonical_role_id": "agile_transformation_manager"},
    {"alias": "Enterprise Agile Transformation Manager", "canonical_role_id": "agile_transformation_manager"},

    # Product Operations & Strategy
    {"alias": "Product Ops Manager", "canonical_role_id": "product_operations_manager"},
    {"alias": "Product Operations Lead", "canonical_role_id": "product_operations_manager"},
    {"alias": "Product Ops Specialist", "canonical_role_id": "product_operations_specialist"},
    {"alias": "Product Operations Executive", "canonical_role_id": "product_operations_specialist"},
    {"alias": "Product Ops Analyst", "canonical_role_id": "product_operations_analyst"},
    {"alias": "Product Management Analyst", "canonical_role_id": "product_operations_analyst"},
    {"alias": "Product Strategy Lead", "canonical_role_id": "product_strategy_manager"},
    {"alias": "Strategic Product Manager", "canonical_role_id": "product_strategy_manager"},
    {"alias": "Product Strategy Specialist", "canonical_role_id": "product_strategy_analyst"},
    {"alias": "Product Planning Analyst", "canonical_role_id": "product_strategy_analyst"},
    {"alias": "Head of Product Management", "canonical_role_id": "product_management_director"},
    {"alias": "VP of Product Management", "canonical_role_id": "product_management_director"},
    {"alias": "Director of Product Operations", "canonical_role_id": "head_of_product_operations"},
    {"alias": "Product Operations Director", "canonical_role_id": "head_of_product_operations"},
    {"alias": "Product Roadmap Manager", "canonical_role_id": "product_planning_manager"},
    {"alias": "Product Portfolio Planning Manager", "canonical_role_id": "product_planning_manager"},
])


ROLE_ALIASES.extend([
    # ============================================================
    # HEALTHCARE & LIFE SCIENCES
    # ============================================================

    # --- Clinical & Medical Practice ---
    {"alias": "GP", "canonical_role_id": "general_practitioner"},
    {"alias": "Primary Care Physician", "canonical_role_id": "general_practitioner"},
    {"alias": "General Practice Doctor", "canonical_role_id": "general_practitioner"},
    {"alias": "Family Doctor", "canonical_role_id": "family_medicine_physician"},
    {"alias": "Family Physician", "canonical_role_id": "family_medicine_physician"},
    {"alias": "Family Medicine Doctor", "canonical_role_id": "family_medicine_physician"},
    {"alias": "Internal Medicine Doctor", "canonical_role_id": "internal_medicine_physician"},
    {"alias": "Internist", "canonical_role_id": "internal_medicine_physician"},
    {"alias": "Medical Specialist", "canonical_role_id": "specialist_physician"},
    {"alias": "Specialist Doctor", "canonical_role_id": "specialist_physician"},
    {"alias": "Consultant Doctor", "canonical_role_id": "consultant_physician"},
    {"alias": "Medical Consultant", "canonical_role_id": "consultant_physician"},
    {"alias": "Surgical Doctor", "canonical_role_id": "surgeon"},
    {"alias": "General Surgery Specialist", "canonical_role_id": "general_surgeon"},
    {"alias": "Emergency Doctor", "canonical_role_id": "emergency_medicine_physician"},
    {"alias": "Emergency Physician", "canonical_role_id": "emergency_medicine_physician"},
    {"alias": "Child Specialist", "canonical_role_id": "pediatrician"},
    {"alias": "Children's Doctor", "canonical_role_id": "pediatrician"},
    {"alias": "Heart Specialist", "canonical_role_id": "cardiologist"},
    {"alias": "Heart Doctor", "canonical_role_id": "cardiologist"},
    {"alias": "Brain Specialist", "canonical_role_id": "neurologist"},
    {"alias": "Nervous System Specialist", "canonical_role_id": "neurologist"},
    {"alias": "Anaesthetist", "canonical_role_id": "anesthesiologist"},
    {"alias": "Anesthesia Physician", "canonical_role_id": "anesthesiologist"},
    {"alias": "Skin Specialist", "canonical_role_id": "dermatologist"},
    {"alias": "Skin Doctor", "canonical_role_id": "dermatologist"},

    # --- Nursing & Patient Care ---
    {"alias": "RN", "canonical_role_id": "registered_nurse"},
    {"alias": "Registered Nursing Professional", "canonical_role_id": "registered_nurse"},
    {"alias": "School Nurse", "canonical_role_id": "registered_nurse"},
    {"alias": "Hospital Nurse", "canonical_role_id": "staff_nurse"},
    {"alias": "Clinical Staff Nurse", "canonical_role_id": "staff_nurse"},
    {"alias": "Advanced Practice Nurse", "canonical_role_id": "nurse_practitioner"},
    {"alias": "Advanced Nurse Practitioner", "canonical_role_id": "nurse_practitioner"},
    {"alias": "Specialist Nurse", "canonical_role_id": "clinical_nurse_specialist"},
    {"alias": "Nursing Clinical Specialist", "canonical_role_id": "clinical_nurse_specialist"},
    {"alias": "Nursing Department Manager", "canonical_role_id": "nurse_manager"},
    {"alias": "Nursing Team Manager", "canonical_role_id": "nurse_manager"},
    {"alias": "Nursing Charge Supervisor", "canonical_role_id": "nursing_supervisor"},
    {"alias": "Critical Care Registered Nurse", "canonical_role_id": "critical_care_nurse"},
    {"alias": "ICU Nurse", "canonical_role_id": "critical_care_nurse"},
    {"alias": "ER Nurse", "canonical_role_id": "emergency_nurse"},
    {"alias": "Emergency Department Nurse", "canonical_role_id": "emergency_nurse"},
    {"alias": "OR Nurse", "canonical_role_id": "operating_room_nurse"},
    {"alias": "Theatre Nurse", "canonical_role_id": "operating_room_nurse"},
    {"alias": "Pediatric Registered Nurse", "canonical_role_id": "pediatric_nurse"},
    {"alias": "Children's Nurse", "canonical_role_id": "pediatric_nurse"},
    {"alias": "Cancer Care Nurse", "canonical_role_id": "oncology_nurse"},
    {"alias": "Oncology Registered Nurse", "canonical_role_id": "oncology_nurse"},
    {"alias": "Community Nursing Specialist", "canonical_role_id": "community_health_nurse"},
    {"alias": "Home Care Nurse", "canonical_role_id": "home_health_nurse"},
    {"alias": "Visiting Nurse", "canonical_role_id": "home_health_nurse"},

    # --- Pharmacy & Pharmaceutical Sciences ---
    {"alias": "Community Drugstore Pharmacist", "canonical_role_id": "community_pharmacist"},
    {"alias": "Clinical Pharmacy Specialist", "canonical_role_id": "clinical_pharmacist"},
    {"alias": "Hospital Clinical Pharmacist", "canonical_role_id": "hospital_pharmacist"},
    {"alias": "Pharmaceutical Researcher", "canonical_role_id": "pharmaceutical_research_scientist"},
    {"alias": "Drug Research Scientist", "canonical_role_id": "pharmaceutical_research_scientist"},
    {"alias": "Drug Formulation Scientist", "canonical_role_id": "formulation_scientist"},
    {"alias": "Pharmaceutical Formulation Researcher", "canonical_role_id": "formulation_scientist"},
    {"alias": "Drug Safety Specialist", "canonical_role_id": "drug_safety_associate"},
    {"alias": "Drug Safety Officer", "canonical_role_id": "drug_safety_associate"},
    {"alias": "Pharmacovigilance Associate", "canonical_role_id": "pharmacovigilance_specialist"},
    {"alias": "PV Specialist", "canonical_role_id": "pharmacovigilance_specialist"},
    {"alias": "Pharmaceutical QC Analyst", "canonical_role_id": "pharmaceutical_quality_control_analyst"},
    {"alias": "Pharma Quality Control Analyst", "canonical_role_id": "pharmaceutical_quality_control_analyst"},
    {"alias": "Pharmaceutical Production Specialist", "canonical_role_id": "pharmaceutical_manufacturing_specialist"},
    {"alias": "Pharma Manufacturing Specialist", "canonical_role_id": "pharmaceutical_manufacturing_specialist"},
    {"alias": "Pharmaceutical Process Validation Specialist", "canonical_role_id": "pharmaceutical_validation_specialist"},
    {"alias": "Pharma Validation Specialist", "canonical_role_id": "pharmaceutical_validation_specialist"},
    {"alias": "Pharmacy Operations Manager", "canonical_role_id": "pharmacy_manager"},

    # --- Allied Health & Rehabilitation ---
    {"alias": "Physical Therapist", "canonical_role_id": "physiotherapist"},
    {"alias": "Physical Therapy Specialist", "canonical_role_id": "physiotherapist"},
    {"alias": "Speech Therapist", "canonical_role_id": "speech_language_pathologist"},
    {"alias": "Speech Pathologist", "canonical_role_id": "speech_language_pathologist"},
    {"alias": "Hearing Specialist", "canonical_role_id": "audiologist"},
    {"alias": "Hearing Healthcare Professional", "canonical_role_id": "audiologist"},
    {"alias": "X-Ray Technician", "canonical_role_id": "radiographer"},
    {"alias": "Radiologic Technologist", "canonical_role_id": "radiographer"},
    {"alias": "Medical Radiology Technologist", "canonical_role_id": "medical_imaging_technologist"},
    {"alias": "Diagnostic Imaging Technologist", "canonical_role_id": "medical_imaging_technologist"},
    {"alias": "Ultrasound Technician", "canonical_role_id": "sonographer"},
    {"alias": "Ultrasound Technologist", "canonical_role_id": "sonographer"},
    {"alias": "Registered Dietitian", "canonical_role_id": "dietitian"},
    {"alias": "Clinical Dietitian", "canonical_role_id": "dietitian"},
    {"alias": "Respiratory Care Practitioner", "canonical_role_id": "respiratory_therapist"},
    {"alias": "Respiratory Care Therapist", "canonical_role_id": "respiratory_therapist"},
    {"alias": "Prosthetics and Orthotics Specialist", "canonical_role_id": "prosthetist_orthotist"},
    {"alias": "Optometry Specialist", "canonical_role_id": "optometrist"},
    {"alias": "Emergency Medical Responder", "canonical_role_id": "paramedic"},
    {"alias": "EMT", "canonical_role_id": "emergency_medical_technician"},
    {"alias": "Ambulance Technician", "canonical_role_id": "emergency_medical_technician"},

    # --- Medical Laboratory & Diagnostics ---
    {"alias": "Medical Lab Technologist", "canonical_role_id": "medical_lab_technologist"},
    {"alias": "Clinical Medical Laboratory Scientist", "canonical_role_id": "medical_lab_scientist"},
    {"alias": "Medical Laboratory Technician", "canonical_role_id": "clinical_lab_technician"},
    {"alias": "Clinical Lab Technician", "canonical_role_id": "clinical_lab_technician"},
    {"alias": "Diagnostic Laboratory Manager", "canonical_role_id": "laboratory_manager"},
    {"alias": "Histology Technologist", "canonical_role_id": "histotechnologist"},
    {"alias": "Histology Technician", "canonical_role_id": "histotechnologist"},
    {"alias": "Cytology Technologist", "canonical_role_id": "cytotechnologist"},
    {"alias": "Cytology Technician", "canonical_role_id": "cytotechnologist"},
    {"alias": "Clinical Microbiology Specialist", "canonical_role_id": "clinical_microbiologist"},
    {"alias": "Medical Laboratory Quality Assurance Specialist", "canonical_role_id": "medical_lab_quality_specialist"},
    {"alias": "Laboratory Quality Specialist", "canonical_role_id": "medical_lab_quality_specialist"},
    {"alias": "Medical Pathologist", "canonical_role_id": "clinical_pathologist"},
    {"alias": "Blood Collection Technician", "canonical_role_id": "phlebotomist"},
    {"alias": "Phlebotomy Technician", "canonical_role_id": "phlebotomist"},
    {"alias": "Blood Bank Technologist", "canonical_role_id": "blood_bank_technologist"},
    {"alias": "Transfusion Laboratory Technologist", "canonical_role_id": "blood_bank_technologist"},
    {"alias": "Molecular Lab Technologist", "canonical_role_id": "molecular_diagnostics_technologist"},
    {"alias": "Molecular Diagnostics Technician", "canonical_role_id": "molecular_diagnostics_technologist"},
    {"alias": "Clinical Chemistry Laboratory Technologist", "canonical_role_id": "clinical_chemistry_technologist"},
    {"alias": "Clinical Biochemistry Technologist", "canonical_role_id": "clinical_chemistry_technologist"},

    # --- Public Health & Healthcare Administration ---
    {"alias": "Public Health Analyst", "canonical_role_id": "public_health_specialist"},
    {"alias": "Public Health Professional", "canonical_role_id": "public_health_specialist"},
    {"alias": "Disease Epidemiologist", "canonical_role_id": "epidemiologist"},
    {"alias": "Public Health Program Officer", "canonical_role_id": "public_health_officer"},
    {"alias": "Healthcare Management Administrator", "canonical_role_id": "healthcare_administrator"},
    {"alias": "Medical Administrator", "canonical_role_id": "healthcare_administrator"},
    {"alias": "Hospital Operations Administrator", "canonical_role_id": "hospital_administrator"},
    {"alias": "Hospital Management Administrator", "canonical_role_id": "hospital_administrator"},
    {"alias": "Healthcare Operations Director", "canonical_role_id": "healthcare_operations_manager"},
    {"alias": "Health Information Administrator", "canonical_role_id": "health_information_manager"},
    {"alias": "Medical Information Manager", "canonical_role_id": "health_information_manager"},
    {"alias": "Healthcare Quality Assurance Manager", "canonical_role_id": "healthcare_quality_manager"},
    {"alias": "Hospital Quality Manager", "canonical_role_id": "healthcare_quality_manager"},
    {"alias": "Medical Records Administrator", "canonical_role_id": "medical_records_officer"},
    {"alias": "Medical Records Executive", "canonical_role_id": "medical_records_officer"},
    {"alias": "Health Services Administrator", "canonical_role_id": "health_services_manager"},
    {"alias": "Infection Control Specialist", "canonical_role_id": "infection_preventionist"},
    {"alias": "Infection Control Practitioner", "canonical_role_id": "infection_preventionist"},
    {"alias": "Healthcare Economist", "canonical_role_id": "health_economist"},
    {"alias": "Community Health Outreach Worker", "canonical_role_id": "community_health_worker"},
    {"alias": "Community Health Assistant", "canonical_role_id": "community_health_worker"},

    # --- Biotechnology & Biomedical Research ---
    {"alias": "Biotechnology Specialist", "canonical_role_id": "biotechnologist"},
    {"alias": "Biotech Scientist", "canonical_role_id": "biotechnologist"},
    {"alias": "Biomedical Researcher", "canonical_role_id": "biomedical_research_scientist"},
    {"alias": "Biomedical Research Associate", "canonical_role_id": "biomedical_research_scientist"},
    {"alias": "Molecular Biology Scientist", "canonical_role_id": "molecular_biologist"},
    {"alias": "Molecular Biology Researcher", "canonical_role_id": "molecular_biologist"},
    {"alias": "Genetics Scientist", "canonical_role_id": "geneticist"},
    {"alias": "Genetics Researcher", "canonical_role_id": "geneticist"},
    {"alias": "Bioinformatics Research Scientist", "canonical_role_id": "bioinformatics_scientist"},
    {"alias": "Computational Biology Scientist", "canonical_role_id": "bioinformatics_scientist"},
    {"alias": "Cell Culture Research Scientist", "canonical_role_id": "cell_culture_scientist"},
    {"alias": "Cell Culture Specialist", "canonical_role_id": "cell_culture_scientist"},
    {"alias": "Bioprocess Research Scientist", "canonical_role_id": "bioprocess_scientist"},
    {"alias": "Bioprocess Development Scientist", "canonical_role_id": "bioprocess_scientist"},
    {"alias": "Microbiology Research Scientist", "canonical_role_id": "microbiologist"},
    {"alias": "Microbiology Scientist", "canonical_role_id": "microbiologist"},
    {"alias": "Immunology Research Scientist", "canonical_role_id": "immunologist"},
    {"alias": "Immunology Scientist", "canonical_role_id": "immunologist"},
    {"alias": "Virology Research Scientist", "canonical_role_id": "virologist"},
    {"alias": "Virology Scientist", "canonical_role_id": "virologist"},
    {"alias": "Protein Research Scientist", "canonical_role_id": "protein_scientist"},
    {"alias": "Protein Biochemist", "canonical_role_id": "protein_scientist"},
    {"alias": "Genomics Research Scientist", "canonical_role_id": "genomics_scientist"},
    {"alias": "Genomics Researcher", "canonical_role_id": "genomics_scientist"},

    # --- Clinical Research & Regulatory Affairs ---
    {"alias": "CRA", "canonical_role_id": "clinical_research_associate"},
    {"alias": "Clinical Trial Monitor", "canonical_role_id": "clinical_research_associate"},
    {"alias": "Clinical Study Coordinator", "canonical_role_id": "clinical_research_coordinator"},
    {"alias": "Clinical Trial Coordinator", "canonical_role_id": "clinical_research_coordinator"},
    {"alias": "Clinical Research Lead", "canonical_role_id": "clinical_research_manager"},
    {"alias": "Clinical Studies Manager", "canonical_role_id": "clinical_research_manager"},
    {"alias": "Clinical Trials Manager", "canonical_role_id": "clinical_trial_manager"},
    {"alias": "Clinical Trial Operations Manager", "canonical_role_id": "clinical_trial_manager"},
    {"alias": "Clinical Data Management Specialist", "canonical_role_id": "clinical_data_manager"},
    {"alias": "Clinical Database Manager", "canonical_role_id": "clinical_data_manager"},
    {"alias": "Regulatory Affairs Officer", "canonical_role_id": "regulatory_affairs_specialist"},
    {"alias": "Regulatory Affairs Associate", "canonical_role_id": "regulatory_affairs_specialist"},
    {"alias": "Regulatory Affairs Lead", "canonical_role_id": "regulatory_affairs_manager"},
    {"alias": "Clinical Research Investigator", "canonical_role_id": "clinical_research_scientist"},
    {"alias": "Clinical Study Scientist", "canonical_role_id": "clinical_research_scientist"},
    {"alias": "Clinical Operations Lead", "canonical_role_id": "clinical_operations_manager"},
    {"alias": "Clinical Trial Coordinator Assistant", "canonical_role_id": "clinical_trial_assistant"},
    {"alias": "Clinical Research Assistant", "canonical_role_id": "clinical_trial_assistant"},
    {"alias": "Clinical QA Specialist", "canonical_role_id": "clinical_quality_assurance_specialist"},
    {"alias": "Clinical Quality Specialist", "canonical_role_id": "clinical_quality_assurance_specialist"},
    {"alias": "Regulatory Submission Associate", "canonical_role_id": "regulatory_submissions_specialist"},
    {"alias": "Regulatory Documentation Specialist", "canonical_role_id": "regulatory_submissions_specialist"},
    {"alias": "Clinical Program Project Manager", "canonical_role_id": "clinical_project_manager"},
])



ROLE_ALIASES.extend([
    # ============================================================
    # OTHER PROFESSIONAL ROLES
    # ============================================================

    # --- Government & Public Administration ---
    {"alias": "Public Administrator", "canonical_role_id": "public_administration_officer"},
    {"alias": "Government Administration Officer", "canonical_role_id": "public_administration_officer"},
    {"alias": "Government Affairs Officer", "canonical_role_id": "government_relations_officer"},
    {"alias": "Government Liaison Officer", "canonical_role_id": "government_relations_officer"},
    {"alias": "Government Officer", "canonical_role_id": "civil_service_officer"},
    {"alias": "Civil Servant", "canonical_role_id": "civil_service_officer"},
    {"alias": "Policy Research Analyst", "canonical_role_id": "policy_analyst"},
    {"alias": "Public Policy Analyst", "canonical_role_id": "policy_analyst"},
    {"alias": "Public Sector Administration Manager", "canonical_role_id": "public_administration_manager"},
    {"alias": "Government Administration Manager", "canonical_role_id": "public_administration_manager"},
    {"alias": "Government Project Officer", "canonical_role_id": "government_program_officer"},
    {"alias": "Public Program Officer", "canonical_role_id": "government_program_officer"},
    {"alias": "City Administrator", "canonical_role_id": "municipal_administrator"},
    {"alias": "Municipal Operations Administrator", "canonical_role_id": "municipal_administrator"},
    {"alias": "Urban Planning Officer", "canonical_role_id": "urban_government_planner"},
    {"alias": "Government Urban Planner", "canonical_role_id": "urban_government_planner"},
    {"alias": "Legislative Affairs Officer", "canonical_role_id": "legislative_affairs_specialist"},
    {"alias": "Government Legislative Affairs Specialist", "canonical_role_id": "legislative_affairs_specialist"},
    {"alias": "Government Consultant", "canonical_role_id": "public_sector_consultant"},
    {"alias": "Public Sector Advisory Consultant", "canonical_role_id": "public_sector_consultant"},
    {"alias": "Diplomat", "canonical_role_id": "diplomatic_officer"},
    {"alias": "Diplomatic Service Officer", "canonical_role_id": "diplomatic_officer"},
    {"alias": "Foreign Affairs Officer", "canonical_role_id": "foreign_service_officer"},
    {"alias": "Foreign Service Diplomat", "canonical_role_id": "foreign_service_officer"},
    {"alias": "Election Officer", "canonical_role_id": "election_administration_officer"},
    {"alias": "Electoral Administration Officer", "canonical_role_id": "election_administration_officer"},

    # --- Policy, International Development & NGOs ---
    {"alias": "NGO Project Officer", "canonical_role_id": "ngo_program_officer"},
    {"alias": "Nonprofit Program Officer", "canonical_role_id": "ngo_program_officer"},
    {"alias": "NGO Project Manager", "canonical_role_id": "ngo_program_manager"},
    {"alias": "Nonprofit Program Manager", "canonical_role_id": "ngo_program_manager"},
    {"alias": "International Development Officer", "canonical_role_id": "international_development_specialist"},
    {"alias": "Development Sector Specialist", "canonical_role_id": "international_development_specialist"},
    {"alias": "Humanitarian Affairs Specialist", "canonical_role_id": "humanitarian_affairs_officer"},
    {"alias": "Humanitarian Officer", "canonical_role_id": "humanitarian_affairs_officer"},
    {"alias": "Humanitarian Program Manager", "canonical_role_id": "humanitarian_project_manager"},
    {"alias": "Humanitarian Project Lead", "canonical_role_id": "humanitarian_project_manager"},
    {"alias": "Grant Program Manager", "canonical_role_id": "grants_manager"},
    {"alias": "Grants and Funding Manager", "canonical_role_id": "grants_manager"},
    {"alias": "NGO Partnership Manager", "canonical_role_id": "ngo_partnerships_manager"},
    {"alias": "Nonprofit Partnerships Manager", "canonical_role_id": "ngo_partnerships_manager"},
    {"alias": "Fundraising Director", "canonical_role_id": "nonprofit_fundraising_manager"},
    {"alias": "Charity Fundraising Manager", "canonical_role_id": "nonprofit_fundraising_manager"},
    {"alias": "Monitoring and Evaluation Specialist", "canonical_role_id": "monitoring_evaluation_learning_specialist"},
    {"alias": "MEL Specialist", "canonical_role_id": "monitoring_evaluation_learning_specialist"},
    {"alias": "Community Development Specialist", "canonical_role_id": "community_development_officer"},
    {"alias": "Community Development Coordinator", "canonical_role_id": "community_development_officer"},
    {"alias": "Livelihood Development Officer", "canonical_role_id": "livelihoods_officer"},
    {"alias": "Livelihood Program Officer", "canonical_role_id": "livelihoods_officer"},
    {"alias": "Social Impact Director", "canonical_role_id": "social_impact_manager"},
    {"alias": "Social Impact Program Manager", "canonical_role_id": "social_impact_manager"},
    {"alias": "Advocacy Manager", "canonical_role_id": "advocacy_campaigns_manager"},
    {"alias": "Campaigns Manager", "canonical_role_id": "advocacy_campaigns_manager"},
    {"alias": "Humanitarian Supply Chain Coordinator", "canonical_role_id": "humanitarian_logistics_coordinator"},
    {"alias": "Emergency Logistics Coordinator", "canonical_role_id": "humanitarian_logistics_coordinator"},

    # --- Research, Think Tanks & Social Sciences ---
    {"alias": "Social Science Researcher", "canonical_role_id": "social_researcher"},
    {"alias": "Social Studies Researcher", "canonical_role_id": "social_researcher"},
    {"alias": "Social Science Specialist", "canonical_role_id": "social_scientist"},
    {"alias": "Social Science Professional", "canonical_role_id": "social_scientist"},
    {"alias": "Sociology Researcher", "canonical_role_id": "sociologist"},
    {"alias": "Sociology Specialist", "canonical_role_id": "sociologist"},
    {"alias": "Political Research Scientist", "canonical_role_id": "political_scientist"},
    {"alias": "Political Science Researcher", "canonical_role_id": "political_scientist"},
    {"alias": "Population Researcher", "canonical_role_id": "demographer"},
    {"alias": "Population Studies Specialist", "canonical_role_id": "demographer"},
    {"alias": "Cultural Anthropologist", "canonical_role_id": "anthropologist"},
    {"alias": "Anthropology Researcher", "canonical_role_id": "anthropologist"},
    {"alias": "Research Associate Fellow", "canonical_role_id": "research_fellow"},
    {"alias": "Academic Research Fellow", "canonical_role_id": "research_fellow"},
    {"alias": "Policy Institute Researcher", "canonical_role_id": "think_tank_researcher"},
    {"alias": "Think Tank Analyst", "canonical_role_id": "think_tank_researcher"},
    {"alias": "Public Policy Research Analyst", "canonical_role_id": "public_policy_researcher"},
    {"alias": "Policy Researcher", "canonical_role_id": "public_policy_researcher"},
    {"alias": "Qualitative Research Analyst", "canonical_role_id": "qualitative_researcher"},
    {"alias": "Qualitative Research Specialist", "canonical_role_id": "qualitative_researcher"},
    {"alias": "Survey Research Analyst", "canonical_role_id": "survey_researcher"},
    {"alias": "Survey Methodology Researcher", "canonical_role_id": "survey_researcher"},
    {"alias": "Program Evaluation Researcher", "canonical_role_id": "evaluation_researcher"},
    {"alias": "Evaluation Specialist Researcher", "canonical_role_id": "evaluation_researcher"},
    {"alias": "Research Program Director", "canonical_role_id": "research_program_manager"},
    {"alias": "Research Project Program Manager", "canonical_role_id": "research_program_manager"},
    {"alias": "Director of Research", "canonical_role_id": "research_director"},
    {"alias": "Head of Research", "canonical_role_id": "research_director"},

    # --- Environment & Sustainability ---
    {"alias": "Environmental Research Scientist", "canonical_role_id": "environmental_scientist"},
    {"alias": "Environmental Science Specialist", "canonical_role_id": "environmental_scientist"},
    {"alias": "Environmental Advisory Consultant", "canonical_role_id": "environmental_consultant"},
    {"alias": "Environmental Management Consultant", "canonical_role_id": "environmental_consultant"},
    {"alias": "Sustainability Consultant", "canonical_role_id": "sustainability_specialist"},
    {"alias": "Sustainability Officer", "canonical_role_id": "sustainability_specialist"},
    {"alias": "Head of Sustainability", "canonical_role_id": "sustainability_manager"},
    {"alias": "Corporate Sustainability Manager", "canonical_role_id": "sustainability_manager"},
    {"alias": "Climate Analyst", "canonical_role_id": "climate_change_analyst"},
    {"alias": "Climate Risk Analyst", "canonical_role_id": "climate_change_analyst"},
    {"alias": "Climate Policy Analyst", "canonical_role_id": "climate_policy_specialist"},
    {"alias": "Climate Policy Advisor", "canonical_role_id": "climate_policy_specialist"},
    {"alias": "Environmental Compliance Officer", "canonical_role_id": "environmental_compliance_specialist"},
    {"alias": "Environmental Regulatory Compliance Specialist", "canonical_role_id": "environmental_compliance_specialist"},
    {"alias": "Environmental Impact Assessment Consultant", "canonical_role_id": "environmental_impact_assessment_specialist"},
    {"alias": "EIA Specialist", "canonical_role_id": "environmental_impact_assessment_specialist"},
    {"alias": "Conservation Specialist", "canonical_role_id": "conservation_officer"},
    {"alias": "Wildlife Conservation Officer", "canonical_role_id": "conservation_officer"},
    {"alias": "Biodiversity Conservation Specialist", "canonical_role_id": "biodiversity_specialist"},
    {"alias": "Biodiversity Officer", "canonical_role_id": "biodiversity_specialist"},
    {"alias": "Waste Management Officer", "canonical_role_id": "waste_management_specialist"},
    {"alias": "Waste Management Consultant", "canonical_role_id": "waste_management_specialist"},
    {"alias": "Renewable Energy Policy Analyst", "canonical_role_id": "renewable_energy_policy_specialist"},
    {"alias": "Clean Energy Policy Specialist", "canonical_role_id": "renewable_energy_policy_specialist"},
    {"alias": "Carbon Accounting Analyst", "canonical_role_id": "carbon_accounting_specialist"},
    {"alias": "Carbon Reporting Specialist", "canonical_role_id": "carbon_accounting_specialist"},
    {"alias": "Environmental Project Manager", "canonical_role_id": "environmental_program_manager"},
    {"alias": "Environmental Program Director", "canonical_role_id": "environmental_program_manager"},

    # --- Agriculture & Agribusiness ---
    {"alias": "Agricultural Agronomist", "canonical_role_id": "agronomist"},
    {"alias": "Crop Agronomist", "canonical_role_id": "agronomist"},
    {"alias": "Agricultural Research Scientist", "canonical_role_id": "agricultural_scientist"},
    {"alias": "Agriculture Scientist", "canonical_role_id": "agricultural_scientist"},
    {"alias": "Agriculture Extension Officer", "canonical_role_id": "agricultural_extension_officer"},
    {"alias": "Agricultural Field Officer", "canonical_role_id": "agricultural_extension_officer"},
    {"alias": "Farm Operations Manager", "canonical_role_id": "farm_manager"},
    {"alias": "Farm Supervisor Manager", "canonical_role_id": "farm_manager"},
    {"alias": "Agriculture Operations Manager", "canonical_role_id": "agricultural_manager"},
    {"alias": "Agricultural Operations Head", "canonical_role_id": "agricultural_manager"},
    {"alias": "Agribusiness Operations Manager", "canonical_role_id": "agribusiness_manager"},
    {"alias": "Agricultural Business Manager", "canonical_role_id": "agribusiness_manager"},
    {"alias": "Agricultural Economics Specialist", "canonical_role_id": "agricultural_economist"},
    {"alias": "Farm Economist", "canonical_role_id": "agricultural_economist"},
    {"alias": "Horticulture Specialist", "canonical_role_id": "horticulturist"},
    {"alias": "Horticulture Officer", "canonical_role_id": "horticulturist"},
    {"alias": "Soil Research Scientist", "canonical_role_id": "soil_scientist"},
    {"alias": "Soil Science Specialist", "canonical_role_id": "soil_scientist"},
    {"alias": "Crop Protection Officer", "canonical_role_id": "crop_protection_specialist"},
    {"alias": "Plant Protection Specialist", "canonical_role_id": "crop_protection_specialist"},
    {"alias": "Livestock Operations Manager", "canonical_role_id": "livestock_manager"},
    {"alias": "Animal Farm Manager", "canonical_role_id": "livestock_manager"},
    {"alias": "Animal Science Researcher", "canonical_role_id": "animal_scientist"},
    {"alias": "Animal Science Specialist", "canonical_role_id": "animal_scientist"},
    {"alias": "Irrigation Engineer Specialist", "canonical_role_id": "irrigation_specialist"},
    {"alias": "Agricultural Irrigation Officer", "canonical_role_id": "irrigation_specialist"},
    {"alias": "Agriculture Inspection Officer", "canonical_role_id": "agricultural_inspector"},
    {"alias": "Agricultural Compliance Inspector", "canonical_role_id": "agricultural_inspector"},

    # --- Real Estate & Property Management ---
    {"alias": "Property Sales Agent", "canonical_role_id": "real_estate_agent"},
    {"alias": "Realty Agent", "canonical_role_id": "real_estate_agent"},
    {"alias": "Real Estate Sales Broker", "canonical_role_id": "real_estate_broker"},
    {"alias": "Property Broker", "canonical_role_id": "real_estate_broker"},
    {"alias": "Property Management Officer", "canonical_role_id": "property_manager"},
    {"alias": "Real Estate Property Manager", "canonical_role_id": "property_manager"},
    {"alias": "Property Administrator Officer", "canonical_role_id": "property_administrator"},
    {"alias": "Property Administration Executive", "canonical_role_id": "property_administrator"},
    {"alias": "Lease Administration Manager", "canonical_role_id": "leasing_manager"},
    {"alias": "Lease Manager", "canonical_role_id": "leasing_manager"},
    {"alias": "Rental Consultant", "canonical_role_id": "leasing_consultant"},
    {"alias": "Property Leasing Consultant", "canonical_role_id": "leasing_consultant"},
    {"alias": "Realty Analyst", "canonical_role_id": "real_estate_analyst"},
    {"alias": "Property Market Analyst", "canonical_role_id": "real_estate_analyst"},
    {"alias": "Real Estate Development Director", "canonical_role_id": "real_estate_development_manager"},
    {"alias": "Property Development Manager", "canonical_role_id": "real_estate_development_manager"},
    {"alias": "Property Valuation Surveyor", "canonical_role_id": "real_estate_valuation_surveyor"},
    {"alias": "Real Estate Valuer", "canonical_role_id": "real_estate_valuation_surveyor"},
    {"alias": "Real Estate Appraiser", "canonical_role_id": "property_appraiser"},
    {"alias": "Property Valuation Appraiser", "canonical_role_id": "property_appraiser"},
    {"alias": "Real Estate Asset Manager", "canonical_role_id": "property_asset_manager"},
    {"alias": "Property Investment Asset Manager", "canonical_role_id": "property_asset_manager"},
    {"alias": "Property Transaction Coordinator", "canonical_role_id": "real_estate_transaction_coordinator"},
    {"alias": "Real Estate Closing Coordinator", "canonical_role_id": "real_estate_transaction_coordinator"},
    {"alias": "Real Estate Acquisition Manager", "canonical_role_id": "property_acquisition_manager"},
    {"alias": "Property Acquisition Specialist", "canonical_role_id": "property_acquisition_manager"},
    {"alias": "Real Estate Investment Portfolio Manager", "canonical_role_id": "real_estate_portfolio_manager"},
    {"alias": "Property Portfolio Manager", "canonical_role_id": "real_estate_portfolio_manager"},

    # --- Security, Defence & Public Safety ---
    {"alias": "Security Guard Officer", "canonical_role_id": "security_officer"},
    {"alias": "Corporate Security Officer", "canonical_role_id": "security_officer"},
    {"alias": "Head of Security", "canonical_role_id": "security_manager"},
    {"alias": "Security Department Manager", "canonical_role_id": "security_manager"},
    {"alias": "Security Operations Director", "canonical_role_id": "security_operations_manager"},
    {"alias": "Security Operations Lead", "canonical_role_id": "security_operations_manager"},
    {"alias": "Security Team Supervisor", "canonical_role_id": "security_supervisor"},
    {"alias": "Security Shift Supervisor", "canonical_role_id": "security_supervisor"},
    {"alias": "Bodyguard", "canonical_role_id": "close_protection_officer"},
    {"alias": "Executive Protection Officer", "canonical_role_id": "close_protection_officer"},
    {"alias": "Corporate Security Director", "canonical_role_id": "corporate_security_manager"},
    {"alias": "Enterprise Security Manager", "canonical_role_id": "corporate_security_manager"},
    {"alias": "Loss Prevention Supervisor", "canonical_role_id": "loss_prevention_manager"},
    {"alias": "Retail Loss Prevention Manager", "canonical_role_id": "loss_prevention_manager"},
    {"alias": "Military Defence Analyst", "canonical_role_id": "defence_analyst"},
    {"alias": "Defence Research Analyst", "canonical_role_id": "defence_analyst"},
    {"alias": "Defence Program Manager", "canonical_role_id": "defence_program_officer"},
    {"alias": "Defence Project Officer", "canonical_role_id": "defence_program_officer"},
    {"alias": "Military Operations Analyst", "canonical_role_id": "military_operations_analyst"},
    {"alias": "Defence Operations Analyst", "canonical_role_id": "military_operations_analyst"},
    {"alias": "Disaster Management Specialist", "canonical_role_id": "emergency_management_specialist"},
    {"alias": "Emergency Preparedness Specialist", "canonical_role_id": "emergency_management_specialist"},
    {"alias": "Emergency Response Officer", "canonical_role_id": "emergency_response_coordinator"},
    {"alias": "Emergency Operations Coordinator", "canonical_role_id": "emergency_response_coordinator"},
    {"alias": "Disaster Risk Management Specialist", "canonical_role_id": "disaster_risk_reduction_specialist"},
    {"alias": "Disaster Risk Reduction Officer", "canonical_role_id": "disaster_risk_reduction_specialist"},
    {"alias": "Fire Safety Supervisor", "canonical_role_id": "fire_safety_officer"},
    {"alias": "Fire Prevention Officer", "canonical_role_id": "fire_safety_officer"},
])


ROLE_ALIASES.extend([
    # ============================================================
    # EDUCATION & TRAINING
    # ============================================================

    # --- Teaching & Classroom Education ---
    {"alias": "Elementary School Teacher", "canonical_role_id": "primary_school_teacher"},
    {"alias": "Elementary Teacher", "canonical_role_id": "primary_school_teacher"},
    {"alias": "Middle School Teacher", "canonical_role_id": "secondary_school_teacher"},
    {"alias": "Secondary Education Teacher", "canonical_role_id": "secondary_school_teacher"},
    {"alias": "Senior School Teacher", "canonical_role_id": "high_school_teacher"},
    {"alias": "High School Educator", "canonical_role_id": "high_school_teacher"},
    {"alias": "Nursery Teacher", "canonical_role_id": "preschool_teacher"},
    {"alias": "Pre-Primary Teacher", "canonical_role_id": "preschool_teacher"},
    {"alias": "Early Years Educator", "canonical_role_id": "early_childhood_educator"},
    {"alias": "Early Years Practitioner", "canonical_role_id": "early_childhood_educator"},
    {"alias": "Special Needs Teacher", "canonical_role_id": "special_education_teacher"},
    {"alias": "Special Needs Educator", "canonical_role_id": "special_education_teacher"},
    {"alias": "Relief Teacher", "canonical_role_id": "substitute_teacher"},
    {"alias": "Supply Teacher", "canonical_role_id": "substitute_teacher"},
    {"alias": "General Classroom Educator", "canonical_role_id": "classroom_teacher"},
    {"alias": "Class Teacher", "canonical_role_id": "classroom_teacher"},
    {"alias": "Discipline-Specific Teacher", "canonical_role_id": "subject_teacher"},
    {"alias": "Subject Specialist Teacher", "canonical_role_id": "subject_teacher"},
    {"alias": "Math Teacher", "canonical_role_id": "mathematics_teacher"},
    {"alias": "Maths Teacher", "canonical_role_id": "mathematics_teacher"},
    {"alias": "STEM Teacher", "canonical_role_id": "science_teacher"},
    {"alias": "Science Educator", "canonical_role_id": "science_teacher"},
    {"alias": "Foreign Language Teacher", "canonical_role_id": "language_teacher"},
    {"alias": "ESL Teacher", "canonical_role_id": "language_teacher"},
    {"alias": "PE Teacher", "canonical_role_id": "physical_education_teacher"},
    {"alias": "Physical Education Instructor", "canonical_role_id": "physical_education_teacher"},
    {"alias": "Classroom Aide", "canonical_role_id": "teaching_assistant"},
    {"alias": "Teacher Aide", "canonical_role_id": "teaching_assistant"},

    # --- Higher Education, University & Administration ---
    {"alias": "University Faculty Professor", "canonical_role_id": "university_professor"},
    {"alias": "Professor of Higher Education", "canonical_role_id": "university_professor"},
    {"alias": "Junior Professor", "canonical_role_id": "assistant_professor"},
    {"alias": "Faculty Assistant Professor", "canonical_role_id": "assistant_professor"},
    {"alias": "Faculty Associate Professor", "canonical_role_id": "associate_professor"},
    {"alias": "Tenured Associate Professor", "canonical_role_id": "associate_professor"},
    {"alias": "University Teaching Lecturer", "canonical_role_id": "lecturer"},
    {"alias": "Academic Lecturer", "canonical_role_id": "lecturer"},
    {"alias": "Principal Lecturer", "canonical_role_id": "senior_lecturer"},
    {"alias": "Lead Lecturer", "canonical_role_id": "senior_lecturer"},
    {"alias": "College Instructor", "canonical_role_id": "university_instructor"},
    {"alias": "Higher Education Instructor", "canonical_role_id": "university_instructor"},
    {"alias": "Adjunct Professor", "canonical_role_id": "adjunct_faculty_member"},
    {"alias": "Part-Time Faculty Member", "canonical_role_id": "adjunct_faculty_member"},
    {"alias": "Admissions Counselor", "canonical_role_id": "university_admissions_officer"},
    {"alias": "University Enrollment Officer", "canonical_role_id": "university_admissions_officer"},
    {"alias": "Academic Counsellor", "canonical_role_id": "academic_advisor"},
    {"alias": "Student Academic Advisor", "canonical_role_id": "academic_advisor"},
    {"alias": "College Registrar", "canonical_role_id": "university_registrar"},
    {"alias": "Academic Registrar", "canonical_role_id": "university_registrar"},
    {"alias": "University Administration Officer", "canonical_role_id": "university_administrator"},
    {"alias": "Higher Education Administrator", "canonical_role_id": "university_administrator"},
    {"alias": "Student Services Officer", "canonical_role_id": "student_affairs_officer"},
    {"alias": "Student Affairs Coordinator", "canonical_role_id": "student_affairs_officer"},
    {"alias": "University Department Administrator", "canonical_role_id": "university_department_coordinator"},
    {"alias": "Academic Department Coordinator", "canonical_role_id": "university_department_coordinator"},
    {"alias": "Academic Program Coordinator", "canonical_role_id": "academic_coordinator"},
    {"alias": "Academic Affairs Coordinator", "canonical_role_id": "academic_coordinator"},

    # --- Corporate Training & Learning Development ---
    {"alias": "Corporate Learning Trainer", "canonical_role_id": "corporate_trainer"},
    {"alias": "Business Trainer", "canonical_role_id": "corporate_trainer"},
    {"alias": "IT Trainer", "canonical_role_id": "technical_trainer"},
    {"alias": "Technology Trainer", "canonical_role_id": "technical_trainer"},
    {"alias": "Soft Skills Trainer", "canonical_role_id": "professional_skills_trainer"},
    {"alias": "Professional Development Trainer", "canonical_role_id": "professional_skills_trainer"},
    {"alias": "On-the-Job Trainer", "canonical_role_id": "workplace_trainer"},
    {"alias": "Workplace Learning Trainer", "canonical_role_id": "workplace_trainer"},
    {"alias": "Training Workshop Facilitator", "canonical_role_id": "training_facilitator"},
    {"alias": "Learning Workshop Facilitator", "canonical_role_id": "training_facilitator"},
    {"alias": "Leadership Skills Trainer", "canonical_role_id": "leadership_development_trainer"},
    {"alias": "Executive Leadership Trainer", "canonical_role_id": "leadership_development_trainer"},
    {"alias": "Employee Development Specialist", "canonical_role_id": "employee_training_specialist"},
    {"alias": "Staff Training Specialist", "canonical_role_id": "employee_training_specialist"},
    {"alias": "Corporate Learning Coordinator", "canonical_role_id": "corporate_training_coordinator"},
    {"alias": "Employee Training Coordinator", "canonical_role_id": "corporate_training_coordinator"},
    {"alias": "Learning Program Manager", "canonical_role_id": "training_program_manager"},
    {"alias": "Corporate Training Program Manager", "canonical_role_id": "training_program_manager"},
    {"alias": "Training Operations Manager", "canonical_role_id": "training_delivery_manager"},
    {"alias": "Learning Delivery Manager", "canonical_role_id": "training_delivery_manager"},
    {"alias": "Learning Session Facilitator", "canonical_role_id": "learning_facilitator"},
    {"alias": "Learning and Development Facilitator", "canonical_role_id": "learning_facilitator"},
    {"alias": "Business Management Trainer", "canonical_role_id": "management_trainer"},
    {"alias": "Management Development Trainer", "canonical_role_id": "management_trainer"},
    {"alias": "Customer Education Specialist", "canonical_role_id": "customer_training_specialist"},
    {"alias": "Customer Enablement Trainer", "canonical_role_id": "customer_training_specialist"},
    {"alias": "Corporate Training Consultant", "canonical_role_id": "training_consultant"},

    # --- Instructional Design & E-Learning ---
    {"alias": "Learning Instructional Designer", "canonical_role_id": "instructional_designer"},
    {"alias": "Instructional Design Specialist", "canonical_role_id": "instructional_designer"},
    {"alias": "Lead Instructional Designer", "canonical_role_id": "senior_instructional_designer"},
    {"alias": "Principal Instructional Designer", "canonical_role_id": "senior_instructional_designer"},
    {"alias": "E-Learning Content Developer", "canonical_role_id": "elearning_developer"},
    {"alias": "Digital Course Developer", "canonical_role_id": "elearning_developer"},
    {"alias": "LXD Designer", "canonical_role_id": "learning_experience_designer"},
    {"alias": "Learning Experience Design Specialist", "canonical_role_id": "learning_experience_designer"},
    {"alias": "Learning Curriculum Designer", "canonical_role_id": "curriculum_designer"},
    {"alias": "Academic Curriculum Designer", "canonical_role_id": "curriculum_designer"},
    {"alias": "Curriculum Development Specialist", "canonical_role_id": "curriculum_developer"},
    {"alias": "Curriculum Development Officer", "canonical_role_id": "curriculum_developer"},
    {"alias": "Digital Education Specialist", "canonical_role_id": "digital_learning_specialist"},
    {"alias": "Digital Learning Consultant", "canonical_role_id": "digital_learning_specialist"},
    {"alias": "Online Course Designer", "canonical_role_id": "online_course_developer"},
    {"alias": "Virtual Course Developer", "canonical_role_id": "online_course_developer"},
    {"alias": "Educational Materials Developer", "canonical_role_id": "educational_content_developer"},
    {"alias": "Education Content Specialist", "canonical_role_id": "educational_content_developer"},
    {"alias": "Learning Materials Writer", "canonical_role_id": "learning_content_writer"},
    {"alias": "Educational Content Writer", "canonical_role_id": "learning_content_writer"},
    {"alias": "Multimedia E-Learning Developer", "canonical_role_id": "multimedia_learning_developer"},
    {"alias": "Digital Multimedia Learning Developer", "canonical_role_id": "multimedia_learning_developer"},
    {"alias": "Educational Technology Specialist", "canonical_role_id": "learning_technology_specialist"},
    {"alias": "EdTech Specialist", "canonical_role_id": "learning_technology_specialist"},
    {"alias": "LMS Administrator", "canonical_role_id": "learning_management_system_administrator"},
    {"alias": "Learning Platform Administrator", "canonical_role_id": "learning_management_system_administrator"},
    {"alias": "E-Learning Project Coordinator", "canonical_role_id": "elearning_project_coordinator"},
    {"alias": "Online Learning Project Coordinator", "canonical_role_id": "elearning_project_coordinator"},

    # --- Academic Research & Educational Assessment ---
    {"alias": "Education Research Scientist", "canonical_role_id": "education_researcher"},
    {"alias": "Educational Researcher", "canonical_role_id": "education_researcher"},
    {"alias": "Education Research Analyst", "canonical_role_id": "educational_research_analyst"},
    {"alias": "Academic Research Analyst in Education", "canonical_role_id": "educational_research_analyst"},
    {"alias": "Education Policy Analyst", "canonical_role_id": "education_policy_researcher"},
    {"alias": "Educational Policy Researcher", "canonical_role_id": "education_policy_researcher"},
    {"alias": "Academic Assessment Specialist", "canonical_role_id": "educational_assessment_specialist"},
    {"alias": "Education Assessment Officer", "canonical_role_id": "educational_assessment_specialist"},
    {"alias": "Educational Measurement Analyst", "canonical_role_id": "educational_measurement_specialist"},
    {"alias": "Assessment Measurement Specialist", "canonical_role_id": "educational_measurement_specialist"},
    {"alias": "Academic Assessment Coordinator", "canonical_role_id": "assessment_coordinator"},
    {"alias": "Testing and Assessment Coordinator", "canonical_role_id": "assessment_coordinator"},
    {"alias": "Exam Officer", "canonical_role_id": "examination_officer"},
    {"alias": "Examinations Administrator", "canonical_role_id": "examination_officer"},
    {"alias": "Controller of Examinations", "canonical_role_id": "examination_controller"},
    {"alias": "University Examination Controller", "canonical_role_id": "examination_controller"},
    {"alias": "Academic QA Specialist", "canonical_role_id": "academic_quality_assurance_specialist"},
    {"alias": "Academic Quality Officer", "canonical_role_id": "academic_quality_assurance_specialist"},
    {"alias": "Institutional Research Officer", "canonical_role_id": "institutional_research_analyst"},
    {"alias": "University Research Analyst", "canonical_role_id": "institutional_research_analyst"},
    {"alias": "Educational Evaluation Specialist", "canonical_role_id": "education_evaluation_specialist"},
    {"alias": "Education Program Evaluation Specialist", "canonical_role_id": "education_evaluation_specialist"},
    {"alias": "Learning Assessment Specialist", "canonical_role_id": "learning_outcomes_assessor"},
    {"alias": "Learning Outcomes Evaluator", "canonical_role_id": "learning_outcomes_assessor"},
    {"alias": "Psychometrician", "canonical_role_id": "psychometric_assessment_specialist"},
    {"alias": "Psychometric Analyst", "canonical_role_id": "psychometric_assessment_specialist"},
    {"alias": "Education Analytics Specialist", "canonical_role_id": "education_data_analyst"},
    {"alias": "Educational Data Analyst", "canonical_role_id": "education_data_analyst"},

    # --- Educational Leadership & Administration ---
    {"alias": "Headteacher", "canonical_role_id": "school_principal"},
    {"alias": "School Head", "canonical_role_id": "school_principal"},
    {"alias": "Deputy Principal", "canonical_role_id": "vice_principal"},
    {"alias": "Assistant Principal", "canonical_role_id": "vice_principal"},
    {"alias": "Headmaster", "canonical_role_id": "school_headmaster"},
    {"alias": "Headmistress", "canonical_role_id": "school_headmaster"},
    {"alias": "School Administration Officer", "canonical_role_id": "school_administrator"},
    {"alias": "School Operations Administrator", "canonical_role_id": "school_administrator"},
    {"alias": "Director of School", "canonical_role_id": "school_director"},
    {"alias": "School Executive Director", "canonical_role_id": "school_director"},
    {"alias": "Director of Academic Affairs", "canonical_role_id": "academic_director"},
    {"alias": "Academic Affairs Director", "canonical_role_id": "academic_director"},
    {"alias": "Education Program Head", "canonical_role_id": "education_program_director"},
    {"alias": "Director of Education Programs", "canonical_role_id": "education_program_director"},
    {"alias": "Education Operations Manager", "canonical_role_id": "education_manager"},
    {"alias": "Education Services Manager", "canonical_role_id": "education_manager"},
    {"alias": "School Operations Director", "canonical_role_id": "school_operations_manager"},
    {"alias": "School Facilities and Operations Manager", "canonical_role_id": "school_operations_manager"},
    {"alias": "Education Program Coordinator", "canonical_role_id": "education_coordinator"},
    {"alias": "Educational Services Coordinator", "canonical_role_id": "education_coordinator"},
    {"alias": "Regional Education Officer", "canonical_role_id": "district_education_officer"},
    {"alias": "District School Education Officer", "canonical_role_id": "district_education_officer"},
    {"alias": "Education Inspector", "canonical_role_id": "school_inspector"},
    {"alias": "School Quality Inspector", "canonical_role_id": "school_inspector"},
    {"alias": "Chief Education Officer", "canonical_role_id": "education_superintendent"},
    {"alias": "Education District Superintendent", "canonical_role_id": "education_superintendent"},
    {"alias": "Education Administration Executive", "canonical_role_id": "education_administration_officer"},
    {"alias": "Education Administrative Officer", "canonical_role_id": "education_administration_officer"},
])


ROLE_ALIASES.extend([
    # ============================================================
    # LEGAL & COMPLIANCE
    # ============================================================

    # --- legal_practice_advisory ---
    {"canonical_role_id": "lawyer", "alias": "Attorney"},
    {"canonical_role_id": "legal_advisor", "alias": "Legal Adviser"},
    {"canonical_role_id": "legal_counsel", "alias": "Counsel"},
    {"canonical_role_id": "solicitor", "alias": "Practising Solicitor"},
    {"canonical_role_id": "barrister", "alias": "Trial Barrister"},
    {"canonical_role_id": "litigation_lawyer", "alias": "Litigation Attorney"},
    {"canonical_role_id": "criminal_defense_lawyer", "alias": "Criminal Defense Attorney"},
    {"canonical_role_id": "civil_litigation_lawyer", "alias": "Civil Litigation Attorney"},
    {"canonical_role_id": "employment_lawyer", "alias": "Employment Attorney"},
    {"canonical_role_id": "family_lawyer", "alias": "Family Law Attorney"},
    {"canonical_role_id": "legal_consultant", "alias": "Legal Advisory Consultant"},
    {"canonical_role_id": "legal_associate", "alias": "Associate Attorney"},
    {"canonical_role_id": "legal_researcher", "alias": "Legal Research Associate"},
    {"canonical_role_id": "paralegal", "alias": "Paralegal Specialist"},

    # --- corporate_commercial_law ---
    {"canonical_role_id": "corporate_lawyer", "alias": "Corporate Attorney"},
    {"canonical_role_id": "commercial_lawyer", "alias": "Commercial Attorney"},
    {"canonical_role_id": "corporate_legal_counsel", "alias": "Corporate Counsel"},
    {"canonical_role_id": "mergers_acquisitions_lawyer", "alias": "M&A Lawyer"},
    {"canonical_role_id": "securities_lawyer", "alias": "Securities Attorney"},
    {"canonical_role_id": "banking_lawyer", "alias": "Banking Attorney"},
    {"canonical_role_id": "capital_markets_lawyer", "alias": "Capital Markets Attorney"},
    {"canonical_role_id": "corporate_governance_lawyer", "alias": "Corporate Governance Attorney"},
    {"canonical_role_id": "business_legal_advisor", "alias": "Business Legal Consultant"},
    {"canonical_role_id": "commercial_contracts_lawyer", "alias": "Commercial Contract Attorney"},
    {"canonical_role_id": "competition_lawyer", "alias": "Competition Law Attorney"},
    {"canonical_role_id": "antitrust_lawyer", "alias": "Antitrust Attorney"},
    {"canonical_role_id": "international_trade_lawyer", "alias": "International Trade Attorney"},
    {"canonical_role_id": "corporate_legal_manager", "alias": "Corporate Legal Affairs Manager"},

    # --- regulatory_affairs_compliance ---
    {"canonical_role_id": "legal_regulatory_affairs_specialist", "alias": "Legal Regulatory Specialist"},
    {"canonical_role_id": "regulatory_compliance_officer", "alias": "Regulatory Compliance Executive"},
    {"canonical_role_id": "regulatory_compliance_manager", "alias": "Regulatory Compliance Lead"},
    {"canonical_role_id": "regulatory_analyst", "alias": "Regulatory Affairs Analyst"},
    {"canonical_role_id": "legal_regulatory_affairs_manager", "alias": "Legal Regulatory Manager"},
    {"canonical_role_id": "regulatory_operations_specialist", "alias": "Regulatory Operations Associate"},
    {"canonical_role_id": "licensing_compliance_specialist", "alias": "Licensing and Compliance Specialist"},
    {"canonical_role_id": "regulatory_inspector", "alias": "Regulatory Compliance Inspector"},
    {"canonical_role_id": "compliance_analyst", "alias": "Compliance Risk Analyst"},
    {"canonical_role_id": "compliance_officer", "alias": "Corporate Compliance Officer"},
    {"canonical_role_id": "compliance_manager", "alias": "Compliance Lead"},
    {"canonical_role_id": "legal_compliance_auditor", "alias": "Legal Compliance Audit Specialist"},
    {"canonical_role_id": "regulatory_strategy_specialist", "alias": "Regulatory Strategy Analyst"},

    # --- governance_ethics_corporate_compliance ---
    {"canonical_role_id": "corporate_governance_specialist", "alias": "Corporate Governance Analyst"},
    {"canonical_role_id": "governance_manager", "alias": "Corporate Governance Manager"},
    {"canonical_role_id": "ethics_officer", "alias": "Business Ethics Officer"},
    {"canonical_role_id": "business_ethics_specialist", "alias": "Business Ethics Consultant"},
    {"canonical_role_id": "corporate_compliance_specialist", "alias": "Corporate Compliance Analyst"},
    {"canonical_role_id": "compliance_director", "alias": "Director of Compliance"},
    {"canonical_role_id": "chief_compliance_officer", "alias": "CCO"},
    {"canonical_role_id": "enterprise_compliance_manager", "alias": "Enterprise Compliance Lead"},
    {"canonical_role_id": "anti_bribery_compliance_specialist", "alias": "Anti-Bribery Specialist"},
    {"canonical_role_id": "anti_money_laundering_specialist", "alias": "AML Specialist"},
    {"canonical_role_id": "financial_crime_compliance_officer", "alias": "Financial Crime Officer"},
    {"canonical_role_id": "conduct_risk_specialist", "alias": "Conduct Risk Analyst"},
    {"canonical_role_id": "whistleblower_program_manager", "alias": "Whistleblowing Program Manager"},
    {"canonical_role_id": "corporate_integrity_officer", "alias": "Corporate Integrity Specialist"},

    # --- contracts_legal_operations ---
    {"canonical_role_id": "contract_manager", "alias": "Commercial Contract Manager"},
    {"canonical_role_id": "contracts_administrator", "alias": "Contract Administrator"},
    {"canonical_role_id": "contracts_specialist", "alias": "Contract Management Specialist"},
    {"canonical_role_id": "contract_analyst", "alias": "Contract Management Analyst"},
    {"canonical_role_id": "contract_negotiation_specialist", "alias": "Contract Negotiator"},
    {"canonical_role_id": "legal_operations_manager", "alias": "Legal Ops Manager"},
    {"canonical_role_id": "legal_operations_analyst", "alias": "Legal Ops Analyst"},
    {"canonical_role_id": "legal_project_manager", "alias": "Legal Projects Manager"},
    {"canonical_role_id": "legal_process_analyst", "alias": "Legal Process Improvement Analyst"},
    {"canonical_role_id": "legal_billing_specialist", "alias": "Legal Billing Analyst"},
    {"canonical_role_id": "legal_documentation_specialist", "alias": "Legal Documentation Analyst"},
    {"canonical_role_id": "legal_secretary", "alias": "Law Firm Secretary"},
    {"canonical_role_id": "legal_executive_assistant", "alias": "Legal Executive Support Assistant"},
    {"canonical_role_id": "matter_management_specialist", "alias": "Legal Matter Management Analyst"},

    # --- intellectual_property_privacy_law ---
    {"canonical_role_id": "intellectual_property_lawyer", "alias": "IP Lawyer"},
    {"canonical_role_id": "patent_attorney", "alias": "Patent Lawyer"},
    {"canonical_role_id": "patent_agent", "alias": "Registered Patent Agent"},
    {"canonical_role_id": "trademark_lawyer", "alias": "Trademark Attorney"},
    {"canonical_role_id": "copyright_lawyer", "alias": "Copyright Attorney"},
    {"canonical_role_id": "ip_legal_counsel", "alias": "Intellectual Property Counsel"},
    {"canonical_role_id": "ip_licensing_specialist", "alias": "IP Licensing Analyst"},
    {"canonical_role_id": "ip_portfolio_manager", "alias": "Intellectual Property Portfolio Manager"},
    {"canonical_role_id": "ip_analyst", "alias": "Intellectual Property Analyst"},
    {"canonical_role_id": "patent_analyst", "alias": "Patent Research Analyst"},
    {"canonical_role_id": "privacy_lawyer", "alias": "Data Privacy Lawyer"},
    {"canonical_role_id": "data_privacy_counsel", "alias": "Privacy Counsel"},
    {"canonical_role_id": "data_protection_officer", "alias": "DPO"},
    {"canonical_role_id": "privacy_compliance_specialist", "alias": "Data Privacy Compliance Specialist"},
])


ROLE_ALIASES.extend([
    # ============================================================
    # DESIGN, ARTS & CREATIVE
    # ============================================================

    # --- graphic_visual_design ---
    {"canonical_role_id": "graphic_designer", "alias": "Graphic Design Artist"},
    {"canonical_role_id": "visual_communication_designer", "alias": "Visual Communications Designer"},
    {"canonical_role_id": "brand_identity_designer", "alias": "Brand Designer"},
    {"canonical_role_id": "visual_design_specialist", "alias": "Visual Design Consultant"},
    {"canonical_role_id": "publication_designer", "alias": "Editorial Designer"},
    {"canonical_role_id": "packaging_designer", "alias": "Packaging Design Specialist"},
    {"canonical_role_id": "digital_graphic_designer", "alias": "Digital Designer"},
    {"canonical_role_id": "marketing_graphic_designer", "alias": "Marketing Designer"},
    {"canonical_role_id": "print_designer", "alias": "Print and Graphic Designer"},
    {"canonical_role_id": "presentation_designer", "alias": "Presentation Design Specialist"},
    {"canonical_role_id": "infographic_designer", "alias": "Infographic Design Specialist"},
    {"canonical_role_id": "creative_artworker", "alias": "Artwork Specialist"},
    {"canonical_role_id": "prepress_designer", "alias": "Prepress Artist"},
    {"canonical_role_id": "design_production_artist", "alias": "Graphic Production Artist"},

    # --- ui_ux_digital_product_design ---
    {"canonical_role_id": "ui_ux_designer", "alias": "User Interface and User Experience Designer"},
    {"canonical_role_id": "ux_designer", "alias": "User Experience Designer"},
    {"canonical_role_id": "ui_designer", "alias": "User Interface Designer"},
    {"canonical_role_id": "digital_product_designer", "alias": "Product Experience Designer"},
    {"canonical_role_id": "ux_researcher", "alias": "User Experience Researcher"},
    {"canonical_role_id": "interaction_designer", "alias": "Interaction Design Specialist"},
    {"canonical_role_id": "service_designer", "alias": "Service Design Specialist"},
    {"canonical_role_id": "user_research_specialist", "alias": "User Research Analyst"},
    {"canonical_role_id": "design_systems_designer", "alias": "Design System Designer"},
    {"canonical_role_id": "accessibility_designer", "alias": "Digital Accessibility Designer"},
    {"canonical_role_id": "information_architect", "alias": "Information Architecture Specialist"},
    {"canonical_role_id": "usability_specialist", "alias": "Usability Analyst"},
    {"canonical_role_id": "experience_design_lead", "alias": "UX Design Lead"},
    {"canonical_role_id": "digital_interface_designer", "alias": "Digital UI Designer"},

    # --- animation_motion_graphics_3d ---
    {"canonical_role_id": "animator", "alias": "Animation Artist"},
    {"canonical_role_id": "two_d_animator", "alias": "2D Animation Artist"},
    {"canonical_role_id": "three_d_animator", "alias": "3D Animation Artist"},
    {"canonical_role_id": "motion_graphics_designer", "alias": "Motion Designer"},
    {"canonical_role_id": "three_d_modeler", "alias": "3D Modeling Artist"},
    {"canonical_role_id": "three_d_artist", "alias": "3D Visual Artist"},
    {"canonical_role_id": "character_animator", "alias": "Character Animation Artist"},
    {"canonical_role_id": "character_designer", "alias": "Character Concept Designer"},
    {"canonical_role_id": "visual_effects_artist", "alias": "VFX Artist"},
    {"canonical_role_id": "compositor", "alias": "Compositing Artist"},
    {"canonical_role_id": "rigging_artist", "alias": "Character Rigging Artist"},
    {"canonical_role_id": "storyboard_artist", "alias": "Storyboard Illustrator"},
    {"canonical_role_id": "technical_artist", "alias": "Technical Art Specialist"},
    {"canonical_role_id": "animation_director", "alias": "Director of Animation"},

    # --- film_video_photography ---
    {"canonical_role_id": "videographer", "alias": "Video Production Specialist"},
    {"canonical_role_id": "video_editor", "alias": "Video Editing Specialist"},
    {"canonical_role_id": "film_editor", "alias": "Motion Picture Editor"},
    {"canonical_role_id": "director_of_photography", "alias": "DOP"},
    {"canonical_role_id": "film_director", "alias": "Motion Picture Director"},
    {"canonical_role_id": "film_producer", "alias": "Motion Picture Producer"},
    {"canonical_role_id": "camera_operator", "alias": "Camera Person"},
    {"canonical_role_id": "photographer", "alias": "Professional Photographer"},
    {"canonical_role_id": "commercial_photographer", "alias": "Advertising Photographer"},
    {"canonical_role_id": "photo_editor", "alias": "Photography Editor"},
    {"canonical_role_id": "colorist", "alias": "Film Colorist"},
    {"canonical_role_id": "production_designer_film", "alias": "Film Art Director"},
    {"canonical_role_id": "post_production_supervisor", "alias": "Post Production Manager"},

    # --- writing_editing_publishing ---
    {"canonical_role_id": "creative_writer", "alias": "Creative Content Writer"},
    {"canonical_role_id": "editorial_writer", "alias": "Editorial Content Writer"},
    {"canonical_role_id": "technical_writer", "alias": "Technical Documentation Writer"},
    {"canonical_role_id": "copy_editor", "alias": "Copyediting Specialist"},
    {"canonical_role_id": "manuscript_editor", "alias": "Manuscript Editing Specialist"},
    {"canonical_role_id": "proofreader", "alias": "Proofreading Specialist"},
    {"canonical_role_id": "book_editor", "alias": "Book Publishing Editor"},
    {"canonical_role_id": "publishing_editor", "alias": "Editorial Publishing Specialist"},
    {"canonical_role_id": "editorial_content_specialist", "alias": "Editorial Content Editor"},
    {"canonical_role_id": "scriptwriter", "alias": "Script Writer"},
    {"canonical_role_id": "screenwriter", "alias": "Screen Writer"},
    {"canonical_role_id": "author", "alias": "Book Author"},
    {"canonical_role_id": "journalist", "alias": "News Journalist"},
    {"canonical_role_id": "publishing_manager", "alias": "Publishing Operations Manager"},

    # --- fashion_textile_interior_design ---
    {"canonical_role_id": "fashion_designer", "alias": "Apparel Designer"},
    {"canonical_role_id": "fashion_illustrator", "alias": "Fashion Sketch Artist"},
    {"canonical_role_id": "textile_designer", "alias": "Fabric Designer"},
    {"canonical_role_id": "fashion_merchandiser", "alias": "Apparel Merchandiser"},
    {"canonical_role_id": "fashion_stylist", "alias": "Personal Fashion Stylist"},
    {"canonical_role_id": "costume_designer", "alias": "Theatrical Costume Designer"},
    {"canonical_role_id": "apparel_technical_designer", "alias": "Garment Technical Designer"},
    {"canonical_role_id": "pattern_maker", "alias": "Garment Pattern Maker"},
    {"canonical_role_id": "interior_designer", "alias": "Interior Space Designer"},
    {"canonical_role_id": "interior_decorator", "alias": "Interior Decoration Specialist"},
    {"canonical_role_id": "interior_space_planner", "alias": "Interior Space Planning Specialist"},
    {"canonical_role_id": "furniture_designer", "alias": "Furniture Design Specialist"},
    {"canonical_role_id": "set_designer", "alias": "Stage Set Designer"},
    {"canonical_role_id": "sustainable_fashion_designer", "alias": "Eco Fashion Designer"},

    # --- fine_arts_illustration_creative_direction ---
    {"canonical_role_id": "fine_artist", "alias": "Fine Arts Artist"},
    {"canonical_role_id": "illustrator", "alias": "Professional Illustrator"},
    {"canonical_role_id": "digital_illustrator", "alias": "Digital Art Illustrator"},
    {"canonical_role_id": "concept_artist", "alias": "Concept Design Artist"},
    {"canonical_role_id": "portrait_artist", "alias": "Portrait Painter"},
    {"canonical_role_id": "visual_artist", "alias": "Contemporary Visual Artist"},
    {"canonical_role_id": "art_director", "alias": "Advertising Art Director"},
    {"canonical_role_id": "creative_director", "alias": "Head of Creative"},
    {"canonical_role_id": "creative_designer", "alias": "Creative Design Specialist"},
    {"canonical_role_id": "mural_artist", "alias": "Mural Painter"},
    {"canonical_role_id": "sculptor", "alias": "Sculpture Artist"},
    {"canonical_role_id": "painter", "alias": "Fine Arts Painter"},
    {"canonical_role_id": "printmaker", "alias": "Printmaking Artist"},
    {"canonical_role_id": "art_curator", "alias": "Curatorial Specialist"},
])


ROLE_ALIASES.extend([
    # ============================================================
    # HOSPITALITY, RETAIL & SKILLED TRADES
    # ============================================================

    # --- hospitality_hotel_management ---
    {"canonical_role_id": "hotel_general_manager", "alias": "General Manager - Hotel"},
    {"canonical_role_id": "hotel_operations_manager", "alias": "Hospitality Operations Manager"},
    {"canonical_role_id": "front_office_manager", "alias": "Hotel Front Office Supervisor"},
    {"canonical_role_id": "front_desk_receptionist", "alias": "Hotel Receptionist"},
    {"canonical_role_id": "guest_relations_executive", "alias": "Guest Relations Officer"},
    {"canonical_role_id": "hotel_concierge", "alias": "Hotel Concierge Executive"},
    {"canonical_role_id": "hotel_reservations_agent", "alias": "Hotel Booking Agent"},
    {"canonical_role_id": "housekeeping_manager", "alias": "Hotel Housekeeping Manager"},
    {"canonical_role_id": "housekeeping_supervisor", "alias": "Housekeeping Team Leader"},
    {"canonical_role_id": "hotel_room_attendant", "alias": "Room Attendant"},
    {"canonical_role_id": "hotel_revenue_manager", "alias": "Hospitality Revenue Manager"},
    {"canonical_role_id": "hotel_guest_services_manager", "alias": "Guest Services Manager"},
    {"canonical_role_id": "hotel_night_auditor", "alias": "Night Auditor"},
    {"canonical_role_id": "hotel_banquet_manager", "alias": "Banquet Operations Manager"},

    # --- food_beverage_services ---
    {"canonical_role_id": "restaurant_manager", "alias": "Restaurant General Manager"},
    {"canonical_role_id": "assistant_restaurant_manager", "alias": "Deputy Restaurant Manager"},
    {"canonical_role_id": "food_beverage_manager", "alias": "F&B Manager"},
    {"canonical_role_id": "food_beverage_supervisor", "alias": "F&B Supervisor"},
    {"canonical_role_id": "restaurant_server", "alias": "Waiter"},
    {"canonical_role_id": "bartender", "alias": "Bar Tender"},
    {"canonical_role_id": "barista", "alias": "Coffee Barista"},
    {"canonical_role_id": "sommelier", "alias": "Wine Sommelier"},
    {"canonical_role_id": "restaurant_host", "alias": "Hostess"},
    {"canonical_role_id": "catering_manager", "alias": "Catering Operations Manager"},
    {"canonical_role_id": "catering_coordinator", "alias": "Catering Events Coordinator"},
    {"canonical_role_id": "banquet_server", "alias": "Banquet Waiter"},
    {"canonical_role_id": "room_service_attendant", "alias": "In-Room Dining Attendant"},
    {"canonical_role_id": "food_service_supervisor", "alias": "Food Service Team Leader"},

    # --- travel_tourism_event_services ---
    {"canonical_role_id": "travel_agent", "alias": "Travel Booking Agent"},
    {"canonical_role_id": "travel_consultant", "alias": "Travel Advisor"},
    {"canonical_role_id": "tour_operator", "alias": "Tour Operations Operator"},
    {"canonical_role_id": "tour_guide", "alias": "Tourist Guide"},
    {"canonical_role_id": "travel_coordinator", "alias": "Travel Arrangements Coordinator"},
    {"canonical_role_id": "travel_operations_manager", "alias": "Travel Services Operations Manager"},
    {"canonical_role_id": "tourism_manager", "alias": "Tourism Operations Manager"},
    {"canonical_role_id": "destination_manager", "alias": "Destination Management Specialist"},
    {"canonical_role_id": "event_planner", "alias": "Events Planner"},
    {"canonical_role_id": "event_coordinator", "alias": "Events Coordinator"},
    {"canonical_role_id": "event_manager", "alias": "Events Manager"},
    {"canonical_role_id": "conference_manager", "alias": "Conference and Events Manager"},
    {"canonical_role_id": "wedding_planner", "alias": "Wedding Coordinator"},
    {"canonical_role_id": "event_production_coordinator", "alias": "Live Event Production Coordinator"},

    # --- retail_store_operations ---
    {"canonical_role_id": "retail_store_manager", "alias": "Store Manager"},
    {"canonical_role_id": "assistant_store_manager", "alias": "Deputy Store Manager"},
    {"canonical_role_id": "retail_department_manager", "alias": "Department Store Manager"},
    {"canonical_role_id": "retail_department_supervisor", "alias": "Retail Department Team Leader"},
    {"canonical_role_id": "retail_operations_manager", "alias": "Retail Business Operations Manager"},
    {"canonical_role_id": "retail_operations_coordinator", "alias": "Retail Operations Executive"},
    {"canonical_role_id": "retail_cashier", "alias": "Store Cashier"},
    {"canonical_role_id": "checkout_operator", "alias": "Checkout Assistant"},
    {"canonical_role_id": "retail_stock_associate", "alias": "Stockroom Associate"},
    {"canonical_role_id": "retail_inventory_associate", "alias": "Inventory Associate"},
    {"canonical_role_id": "retail_receiving_clerk", "alias": "Goods Receiving Clerk"},
    {"canonical_role_id": "retail_inventory_controller", "alias": "Retail Stock Controller"},
    {"canonical_role_id": "retail_replenishment_associate", "alias": "Shelf Replenishment Associate"},
    {"canonical_role_id": "retail_buyer", "alias": "Merchandise Buyer"},

    # --- culinary_arts_food_production ---
    {"canonical_role_id": "executive_chef", "alias": "Head Executive Chef"},
    {"canonical_role_id": "head_chef", "alias": "Kitchen Head Chef"},
    {"canonical_role_id": "sous_chef", "alias": "Second Chef"},
    {"canonical_role_id": "chef_de_partie", "alias": "Station Chef"},
    {"canonical_role_id": "commis_chef", "alias": "Junior Chef"},
    {"canonical_role_id": "line_cook", "alias": "Line Chef"},
    {"canonical_role_id": "prep_cook", "alias": "Food Preparation Cook"},
    {"canonical_role_id": "pastry_chef", "alias": "Pastry Cook"},
    {"canonical_role_id": "professional_baker", "alias": "Commercial Baker"},
    {"canonical_role_id": "cake_decorator", "alias": "Cake Artist"},
    {"canonical_role_id": "butcher", "alias": "Meat Cutter"},
    {"canonical_role_id": "fishmonger", "alias": "Fish Seller"},
    {"canonical_role_id": "food_production_supervisor", "alias": "Food Manufacturing Supervisor"},
    {"canonical_role_id": "kitchen_manager", "alias": "Kitchen Operations Manager"},

    # --- construction_building_trades ---
    {"canonical_role_id": "construction_foreman", "alias": "Building Construction Foreman"},
    {"canonical_role_id": "construction_site_supervisor", "alias": "Site Construction Supervisor"},
    {"canonical_role_id": "carpenter", "alias": "Joiner"},
    {"canonical_role_id": "mason", "alias": "Stone Mason"},
    {"canonical_role_id": "bricklayer", "alias": "Brick Mason"},
    {"canonical_role_id": "plasterer", "alias": "Plastering Specialist"},
    {"canonical_role_id": "roofer", "alias": "Roofing Specialist"},
    {"canonical_role_id": "construction_painter", "alias": "Building Painter"},
    {"canonical_role_id": "tile_setter", "alias": "Tile Installer"},
    {"canonical_role_id": "drywall_installer", "alias": "Drywall Fitter"},
    {"canonical_role_id": "glazier", "alias": "Glass Installer"},
    {"canonical_role_id": "flooring_installer", "alias": "Floor Layer"},
    {"canonical_role_id": "scaffolder", "alias": "Scaffolding Installer"},
    {"canonical_role_id": "concrete_finisher", "alias": "Concrete Surface Finisher"},

    # --- electrical_plumbing_mechanical_trades ---
    {"canonical_role_id": "electrician", "alias": "Electrical Installer"},
    {"canonical_role_id": "electrical_technician", "alias": "Electrical Maintenance Technician"},
    {"canonical_role_id": "plumber", "alias": "Plumbing Technician"},
    {"canonical_role_id": "pipefitter", "alias": "Industrial Pipe Fitter"},
    {"canonical_role_id": "hvac_technician", "alias": "HVAC Service Technician"},
    {"canonical_role_id": "refrigeration_technician", "alias": "Refrigeration Service Technician"},
    {"canonical_role_id": "appliance_repair_technician", "alias": "Home Appliance Repair Technician"},
    {"canonical_role_id": "industrial_maintenance_technician", "alias": "Industrial Maintenance Mechanic"},
    {"canonical_role_id": "welder", "alias": "Welding Technician"},
    {"canonical_role_id": "elevator_technician", "alias": "Lift Technician"},
    {"canonical_role_id": "solar_panel_installer", "alias": "Solar PV Installer"},
    {"canonical_role_id": "fire_alarm_technician", "alias": "Fire Detection System Technician"},
    {"canonical_role_id": "building_automation_technician", "alias": "Building Management Systems Technician"},
    {"canonical_role_id": "sheet_metal_worker", "alias": "Sheet Metal Fabricator"},

    # --- automotive_repair_maintenance_services ---
    {"canonical_role_id": "automotive_service_technician", "alias": "Automotive Repair Technician"},
    {"canonical_role_id": "auto_mechanic", "alias": "Car Mechanic"},
    {"canonical_role_id": "diesel_mechanic", "alias": "Diesel Engine Mechanic"},
    {"canonical_role_id": "motorcycle_mechanic", "alias": "Motorbike Mechanic"},
    {"canonical_role_id": "auto_electrician", "alias": "Automotive Electrical Technician"},
    {"canonical_role_id": "vehicle_diagnostics_technician", "alias": "Automotive Diagnostics Technician"},
    {"canonical_role_id": "automotive_service_advisor", "alias": "Service Advisor - Automotive"},
    {"canonical_role_id": "automotive_service_manager", "alias": "Automotive Workshop Manager"},
    {"canonical_role_id": "auto_body_repair_technician", "alias": "Vehicle Body Repair Technician"},
    {"canonical_role_id": "automotive_painter", "alias": "Vehicle Spray Painter"},
    {"canonical_role_id": "tire_service_technician", "alias": "Tyre Technician"},
    {"canonical_role_id": "wheel_alignment_technician", "alias": "Wheel Alignment Specialist"},
    {"canonical_role_id": "vehicle_inspector", "alias": "Automotive Vehicle Inspector"},
    {"canonical_role_id": "fleet_maintenance_technician", "alias": "Fleet Service Technician"},
])

# ============================================================
# EXTENDED JOB TAXONOMY
# Additional canonical roles and aliases
# Keep new additions in this section.
# ============================================================

CANONICAL_ROLES_EXTENDED = [
    # Add genuinely new canonical roles here.
    {
        "id": "computer_science_teacher",
        "name": "Computer Science Teacher",
        "professional_field_id": "education_training",
        "subfield_id": "teaching_classroom_education",
        "description": "Teaches computer science concepts, programming, computational thinking, and related technology subjects in educational settings.",
        "is_active": True,
    },
]

ROLE_ALIASES_EXTENDED = [
    # --- Education ---
    {
        "alias": "Computer Science Educator",
        "canonical_role_id": "computer_science_teacher",
        "is_active": True,
    },


    # --- Software Engineering ---
    {
        "alias": "Software Development Engineer",
        "canonical_role_id": "software_engineer",
        "is_active": True,
    },

]

# Register extended entries with the main taxonomy lists.
CANONICAL_ROLES.extend(CANONICAL_ROLES_EXTENDED)
ROLE_ALIASES.extend(ROLE_ALIASES_EXTENDED)

# ============================================================
# CROSS-FIELD ROLE MAPPINGS
# Additional professional-field associations for existing roles.
# Primary professional fields and subfields remain unchanged.
# ============================================================

ROLE_CROSS_FIELD_MAPPINGS = {

    # --- Product & Project Management -> Technology & IT ---
    "technical_product_manager": ["technology_it"],
    "it_project_manager": ["technology_it"],
    "technical_program_manager": ["technology_it"],
    "release_train_engineer": ["technology_it"],

    # --- Data & Analytics -> Technology & IT ---
    "data_engineer": ["technology_it"],
    "cloud_data_engineer": ["technology_it"],
    "analytics_engineer": ["technology_it"],
    "data_scientist": ["technology_it"],
    "machine_learning_engineer": ["technology_it"],
    "business_intelligence_developer": ["technology_it"],

    # --- Design, Arts & Creative -> Technology & IT ---
    "ui_ux_designer": ["technology_it"],
    "ux_designer": ["technology_it"],
    "ui_designer": ["technology_it"],
    "digital_product_designer": ["technology_it"],
    "interaction_designer": ["technology_it"],
    "design_systems_designer": ["technology_it"],
    "accessibility_designer": ["technology_it"],
    "digital_interface_designer": ["technology_it"],
    "ux_researcher": ["technology_it"],
}