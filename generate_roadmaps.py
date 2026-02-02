#!/usr/bin/env python3
"""
Generate remaining roadmap pages for the Alison Career Roadmaps blog
"""

roadmaps = [
    {
        "filename": "cloud-computing-engineer.md",
        "title": "☁️ Cloud Computing Engineer",
        "overview": "Design and manage cloud-based systems and infrastructure for scalable computing solutions.",
        "salary_entry": "$75,000 - $100,000",
        "salary_mid": "$100,000 - $140,000",
        "salary_senior": "$140,000 - $190,000+",
        "outlook": "Excellent",
        "phases": [
            ("Foundation", "Beginner", "6-8 hours", [
                ("Cloud Computing for Absolute Beginners", "2-3 hours", "Cloud basics, IaaS model, key terms", "https://alison.com/course/cloud-computing-for-absolute-beginners-iaas"),
                ("Cloud Database Technologies and Services", "2-3 hours", "DBaaS, Azure, AWS, GCP", "https://alison.com/course/cloud-computing-database-technologies-and-services")
            ]),
            ("AWS Fundamentals", "Intermediate", "6-8 hours", [
                ("Amazon Web Services: Basic", "2-3 hours", "AWS introduction, core services", "https://alison.com/tag/aws"),
                ("Amazon Web Services: Intermediate", "2-3 hours", "Advanced AWS features", "https://alison.com/tag/aws")
            ]),
            ("AWS Specialization", "Advanced", "16-20 hours", [
                ("Diploma in Amazon Web Services", "8-10 hours", "AWS platform, security, pricing, support", "https://alison.com/course/diploma-in-amazon-web-services"),
                ("Advanced Diploma in Cloud Computing for AWS", "8-10 hours", "EC2, AMI, disaster recovery, SSH, S3, CLI", "https://alison.com/course/advanced-diploma-in-cloud-computing-for-amazon-web-services")
            ])
        ],
        "career_path": "Cloud Support → Cloud Engineer → Senior Cloud Engineer → Cloud Architect",
        "tools": ["AWS", "Azure", "Google Cloud", "Terraform", "Docker", "Kubernetes"],
        "total_time": "45-65 hours"
    },
    {
        "filename": "software-developer.md",
        "title": "💻 Software Developer/Engineer",
        "overview": "Create applications, systems, and software solutions across various platforms.",
        "salary_entry": "$65,000 - $90,000",
        "salary_mid": "$90,000 - $130,000",
        "salary_senior": "$130,000 - $180,000+",
        "outlook": "Excellent",
        "phases": [
            ("Programming Foundations", "Beginner", "6-8 hours", [
                ("Introduction to Programming with Python", "2-3 hours", "Python basics, functions, variables, loops", "https://alison.com/course/introduction-to-programming-with-python-revised"),
                ("Python Fundamentals", "2-3 hours", "Python syntax, data types, modules", "https://alison.com/course/python-fundamentals")
            ]),
            ("Core Python Development", "Intermediate", "16-22 hours", [
                ("Diploma in Python Programming", "8-10 hours", "Visual Studio, data handling, functions", "https://alison.com/course/diploma-in-python-programming-revised"),
                ("Programming Using Python", "3-5 hours", "Comprehensive Python programming", "https://alison.com/course/programming-using-python")
            ]),
            ("Web Development", "Intermediate", "10-15 hours", [
                ("Web Page Design Using HTML5 and CSS3", "2-3 hours", "Web fundamentals", "https://alison.com/tag/programming"),
                ("Web Design with HTML", "8-10 hours", "Complete web design", "https://alison.com/tag/programming")
            ])
        ],
        "career_path": "Junior Developer → Developer → Senior Developer → Lead Developer → Architect",
        "tools": ["Python", "JavaScript", "Git", "VS Code", "React", "Node.js"],
        "total_time": "40-60 hours"
    },
    {
        "filename": "project-manager.md",
        "title": "📋 Project Manager",
        "overview": "Oversee projects across technology, construction, and business sectors to ensure timely and budget-conscious delivery.",
        "salary_entry": "$60,000 - $85,000",
        "salary_mid": "$85,000 - $120,000",
        "salary_senior": "$120,000 - $160,000+",
        "outlook": "Very Good",
        "phases": [
            ("Project Management Fundamentals", "Beginner", "8-12 hours", [
                ("Introduction to Project Management", "2-3 hours", "PM basics, methodologies", "https://alison.com/tag/project-management"),
                ("Diploma in Project Management", "8-10 hours", "Comprehensive PM skills", "https://alison.com/tag/project-management")
            ]),
            ("Agile and Scrum", "Intermediate", "6-8 hours", [
                ("Agile Project Management", "2-3 hours", "Agile methodologies", "https://alison.com/tag/project-management"),
                ("Scrum Master Certification Prep", "3-4 hours", "Scrum framework", "https://alison.com/tag/project-management")
            ]),
            ("Leadership and Communication", "Intermediate", "6-8 hours", [
                ("Leadership in Project Management", "2-3 hours", "Team leadership", "https://alison.com/tag/leadership"),
                ("Business Communication", "2-3 hours", "Stakeholder management", "https://alison.com/tag/business")
            ])
        ],
        "career_path": "Project Coordinator → Project Manager → Senior PM → Program Manager → PMO Director",
        "tools": ["MS Project", "Jira", "Asana", "Trello", "Slack", "MS Office"],
        "total_time": "30-45 hours"
    },
    {
        "filename": "ux-designer.md",
        "title": "🎨 UX Designer",
        "overview": "Create intuitive and engaging digital experiences for applications and websites.",
        "salary_entry": "$55,000 - $75,000",
        "salary_mid": "$75,000 - $105,000",
        "salary_senior": "$105,000 - $145,000+",
        "outlook": "Very Good",
        "phases": [
            ("Design Foundations", "Beginner", "8-10 hours", [
                ("Introduction to Web Design", "2-3 hours", "Web design basics", "https://alison.com/tag/web-design"),
                ("HTML and CSS Basics", "3-4 hours", "Frontend fundamentals", "https://alison.com/tag/web-design")
            ]),
            ("UX Fundamentals", "Intermediate", "8-12 hours", [
                ("User Experience Design", "3-4 hours", "UX principles", "https://alison.com/tag/design"),
                ("UI/UX Design Course", "4-6 hours", "Interface design", "https://alison.com/tag/design")
            ]),
            ("Tools and Technologies", "Intermediate", "10-15 hours", [
                ("Graphic Design Basics", "3-5 hours", "Design principles", "https://alison.com/tag/graphic-design"),
                ("Responsive Web Design", "4-6 hours", "Mobile-first design", "https://alison.com/tag/web-design")
            ])
        ],
        "career_path": "Junior UX Designer → UX Designer → Senior UX Designer → Lead Designer → UX Director",
        "tools": ["Figma", "Adobe XD", "Sketch", "InVision", "Miro", "Photoshop"],
        "total_time": "30-45 hours"
    },
    {
        "filename": "financial-analyst.md",
        "title": "💰 Financial Analyst",
        "overview": "Provide investment guidance and financial planning services by analyzing financial data and market trends.",
        "salary_entry": "$55,000 - $75,000",
        "salary_mid": "$75,000 - $105,000",
        "salary_senior": "$105,000 - $145,000+",
        "outlook": "Good",
        "phases": [
            ("Accounting Foundations", "Beginner", "8-12 hours", [
                ("Introduction to Accounting", "2-3 hours", "Accounting basics", "https://alison.com/tag/accounting"),
                ("Financial Accounting", "4-6 hours", "Financial statements", "https://alison.com/tag/accounting")
            ]),
            ("Financial Analysis", "Intermediate", "10-15 hours", [
                ("Financial Management", "3-5 hours", "Corporate finance", "https://alison.com/tag/finance"),
                ("Investment Analysis", "4-6 hours", "Investment evaluation", "https://alison.com/tag/finance")
            ]),
            ("Data Analysis Tools", "Intermediate", "8-10 hours", [
                ("Excel for Financial Analysis", "3-4 hours", "Advanced Excel", "https://alison.com/tag/excel"),
                ("Financial Modeling", "4-6 hours", "Building models", "https://alison.com/tag/finance")
            ])
        ],
        "career_path": "Junior Analyst → Financial Analyst → Senior Analyst → Finance Manager → CFO",
        "tools": ["Excel", "Bloomberg", "Power BI", "SQL", "Python", "Tableau"],
        "total_time": "30-45 hours"
    }
]

def generate_roadmap(roadmap_data):
    """Generate a roadmap markdown file"""
    
    md_content = f"""# {roadmap_data['title']}

[← Back to All Roadmaps](../README.md)

## 📋 Career Overview

{roadmap_data['overview']}

### Salary Expectations
- **Entry Level:** ${roadmap_data['salary_entry']}/year
- **Mid Level:** ${roadmap_data['salary_mid']}/year
- **Senior Level:** ${roadmap_data['salary_senior']}/year

### Job Market Outlook
📈 **{roadmap_data['outlook']}**

---

## 🗺️ Learning Roadmap

"""
    
    # Add phases
    for i, (phase_name, difficulty, time, courses) in enumerate(roadmap_data['phases'], 1):
        md_content += f"### PHASE {i}: {phase_name} ({difficulty}) - {time}\n\n"
        
        for j, (course_name, duration, topics, link) in enumerate(courses, 1):
            md_content += f"#### Course {j}: {course_name}\n"
            md_content += f"- **Duration:** {duration}\n"
            md_content += f"- **Topics:** {topics}\n"
            md_content += f"- **Link:** [{course_name}]({link})\n\n"
        
        md_content += "---\n\n"
    
    # Add career progression
    md_content += f"""## 💼 Career Progression

```
{roadmap_data['career_path']}
```

---

## 🛠️ Essential Tools

"""
    
    for tool in roadmap_data['tools']:
        md_content += f"- **{tool}**\n"
    
    md_content += f"""

---

## 🎯 Project Ideas

### Beginner Projects
1. Build foundational skills with simple projects
2. Practice with tutorials and guided exercises
3. Create a portfolio to showcase your work

### Intermediate Projects
1. Take on more complex challenges
2. Contribute to open source projects
3. Build real-world applications

### Advanced Projects
1. Lead complete projects from start to finish
2. Mentor others and share your knowledge
3. Innovate and create new solutions

---

## 💡 Tips for Success

1. **Practice Consistently** - Dedicate time every day
2. **Build Projects** - Apply what you learn
3. **Network** - Connect with professionals
4. **Stay Updated** - Follow industry trends
5. **Get Certified** - Pursue relevant certifications

---

## 🔗 Quick Links

- [Back to All Roadmaps](../README.md)
- [Browse Alison Courses](https://alison.com)
- [Start Learning](https://alison.com/sign-up)

---

**Total Learning Time:** {roadmap_data['total_time']}

**Recommended Study Schedule:** 3-6 months at 8-12 hours/week

---

*Last Updated: February 2026*
"""
    
    return md_content

# Generate all roadmap files
for roadmap in roadmaps:
    content = generate_roadmap(roadmap)
    with open(f"roadmaps/{roadmap['filename']}", 'w') as f:
        f.write(content)
    print(f"Created {roadmap['filename']}")

print("\nAll roadmaps generated successfully!")
