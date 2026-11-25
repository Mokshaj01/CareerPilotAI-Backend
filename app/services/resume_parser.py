import google.generativeai as genai
from typing import Dict, Any, List
import json
import PyPDF2
import docx
from io import BytesIO
import re

from app.core.config import settings

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

class ResumeParser:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-3.6-flash')
        
    def extract_text_from_pdf(self, file_content: bytes) -> str:
        """Extract text from PDF file"""
        try:
            pdf_reader = PyPDF2.PdfReader(BytesIO(file_content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    def extract_text_from_docx(self, file_content: bytes) -> str:
        """Extract text from DOCX file"""
        try:
            doc = docx.Document(BytesIO(file_content))
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            raise Exception(f"Error extracting text from DOCX: {str(e)}")
    
    def extract_text_from_file(self, file_content: bytes, file_type: str) -> str:
        """Extract text based on file type"""
        if file_type.lower() == 'pdf':
            return self.extract_text_from_pdf(file_content)
        elif file_type.lower() in ['docx', 'doc']:
            return self.extract_text_from_docx(file_content)
        else:
            raise Exception(f"Unsupported file type: {file_type}")
    
    def parse_resume_with_gemini(self, resume_text: str) -> Dict[str, Any]:
        """Parse resume text using Gemini AI"""
        prompt = f"""
        Parse the following resume text and extract structured information in JSON format.
        Please extract the following sections:

        1. personal_info: {{
            "name": "",
            "email": "",
            "phone": "",
            "location": "",
            "linkedin": "",
            "github": "",
            "portfolio": "",
            "summary": ""
        }}

        2. experience: [{{
            "company": "",
            "position": "",
            "start_date": "",
            "end_date": "",
            "duration": "",
            "location": "",
            "description": "",
            "key_achievements": []
        }}]

        3. skills: {{
            "technical_skills": [],
            "programming_languages": [],
            "frameworks_libraries": [],
            "databases": [],
            "tools": [],
            "soft_skills": []
        }}

        4. education: [{{
            "institution": "",
            "degree": "",
            "field_of_study": "",
            "start_date": "",
            "end_date": "",
            "gpa": "",
            "location": "",
            "relevant_coursework": []
        }}]

        5. projects: [{{
            "name": "",
            "description": "",
            "technologies": [],
            "start_date": "",
            "end_date": "",
            "url": "",
            "key_features": []
        }}]

        6. certifications: [{{
            "name": "",
            "issuer": "",
            "issue_date": "",
            "expiry_date": "",
            "credential_id": "",
            "url": ""
        }}]

        7. languages: [{{
            "language": "",
            "proficiency": ""
        }}]

        Please return only valid JSON without any additional text or formatting.

        Resume Text:
        {resume_text}
        """
        
        try:
            response = self.model.generate_content(prompt)
            parsed_text = response.text.strip()
            
            # Clean up the response to ensure it's valid JSON
            if parsed_text.startswith('```json'):
                parsed_text = parsed_text[7:]
            if parsed_text.endswith('```'):
                parsed_text = parsed_text[:-3]
            
            parsed_data = json.loads(parsed_text)
            return parsed_data
            
        except json.JSONDecodeError as e:
            # If JSON parsing fails, try to extract information manually
            return self._fallback_parsing(resume_text)
        except Exception as e:
            raise Exception(f"Error parsing resume with Gemini: {str(e)}")
    
    def _fallback_parsing(self, resume_text: str) -> Dict[str, Any]:
        """Fallback parsing method if Gemini fails"""
        # Basic regex-based parsing as fallback
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_pattern = r'(\+\d{1,3}\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        
        emails = re.findall(email_pattern, resume_text)
        phones = re.findall(phone_pattern, resume_text)
        
        return {
            "personal_info": {
                "name": "",
                "email": emails[0] if emails else "",
                "phone": phones[0] if phones else "",
                "location": "",
                "linkedin": "",
                "github": "",
                "portfolio": "",
                "summary": ""
            },
            "experience": [],
            "skills": {
                "technical_skills": [],
                "programming_languages": [],
                "frameworks_libraries": [],
                "databases": [],
                "tools": [],
                "soft_skills": []
            },
            "education": [],
            "projects": [],
            "certifications": [],
            "languages": []
        }
    
    def extract_skills_list(self, parsed_data: Dict[str, Any]) -> List[str]:
        """Extract all skills into a flat list"""
        skills = []
        skills_section = parsed_data.get("skills", {})
        
        for skill_category in skills_section.values():
            if isinstance(skill_category, list):
                skills.extend(skill_category)
        
        return list(set(skills))  # Remove duplicates
    
    def extract_experience_text(self, parsed_data: Dict[str, Any]) -> str:
        """Extract experience as concatenated text"""
        experience_text = ""
        for exp in parsed_data.get("experience", []):
            experience_text += f"{exp.get('position', '')} at {exp.get('company', '')}. "
            experience_text += f"{exp.get('description', '')} "
            for achievement in exp.get('key_achievements', []):
                experience_text += f"{achievement} "
        
        return experience_text.strip()
    
    def extract_education_text(self, parsed_data: Dict[str, Any]) -> str:
        """Extract education as concatenated text"""
        education_text = ""
        for edu in parsed_data.get("education", []):
            education_text += f"{edu.get('degree', '')} in {edu.get('field_of_study', '')} "
            education_text += f"from {edu.get('institution', '')}. "
            for course in edu.get('relevant_coursework', []):
                education_text += f"{course} "
        
        return education_text.strip()
    
    def extract_projects_text(self, parsed_data: Dict[str, Any]) -> str:
        """Extract projects as concatenated text"""
        projects_text = ""
        for project in parsed_data.get("projects", []):
            projects_text += f"{project.get('name', '')}: {project.get('description', '')} "
            projects_text += f"Technologies: {', '.join(project.get('technologies', []))} "
        
        return projects_text.strip()
    
    def extract_certifications_text(self, parsed_data: Dict[str, Any]) -> str:
        """Extract certifications as concatenated text"""
        certifications_text = ""
        for cert in parsed_data.get("certifications", []):
            certifications_text += f"{cert.get('name', '')} from {cert.get('issuer', '')} "
        
        return certifications_text.strip()

# Initialize parser instance
resume_parser = ResumeParser()


