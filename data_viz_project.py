# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:21:29 2024

@author: Nicolas Dupont
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


custom_css = """
<style>
    .stApp {
        background: linear-gradient(135deg, rgba(139, 0, 0, 0.8), rgba(0, 0, 0, 1)); /* Gradient from dark red to black */
        color: #FFFFFF;  /* White text color for contrast */
    }
    .stButton {
        background-color: #F63366;  
        color: white;            
    }
    .stSidebar {
        background-color: #000000;   
        color: #FFFFFF;             
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

page = st.sidebar.selectbox("Choose a page", ["Home", "Data Visualization"])

# Home page
if page == "Home":
    add_selectbox = st.sidebar.title(
        "Hello, my name is :red[Nicolas Dupont] and i am in the master Data & AI")

    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🌟 Welcome to my dashboard!</h1>", unsafe_allow_html=True)

    
    st.snow()

    # Section 1 : General Presentation
    st.header("A little bit about me ? 🤔")
    st.markdown("""
    I'm Nicolas, i'm 21 years old and here's a little snipet about me. Currently in the Master "Data & AI" at Efrei Paris", i'm really interested in the field of AI and its infinite possibilites.
    """)

    st.divider()

    # Section 2 : Personal career
    st.header("My professional career 🚀")
    st.markdown("""
    Since the beginning of my studies, i acquired many skills, computer science wise and soft skills
    - 🎓 **Education** : Studying at EFREI Paris, a french engineering school
    - 🏢 **Career** : Worked a month in a finance company / worked in a commercial company for a month
    - 🌍 **Trips** : Studied a semester at the University of California of Irvine in 2023
    """)

    st.divider()

    # Section 3 : My skills
    st.header("My skills 💪")
    st.markdown("""
    Some hard and soft skills i acquired during my studies :
    """)

    st.markdown("""
    - 💻 **Programmation** : Python, Java, C
    - 🌐 **Web development** : Javascript, HTML, CSS
    - 📊 **Data Analysis** : Pandas, NumPy, Matplotlib
    - 🤖 **Machine Learning** : Scikit-learn, TensorFlow, Sk-learn
    """)

    st.divider()

    # Section 4: My projects and academic accomplishments
    st.header("My projects and academic accomplishments 🛠️")
    st.markdown("""
    Some projects i did during my studies :
    """)

    # Display the projects
    st.markdown("""
    - 🧠 **Certification NLP**: Acquired a certification in Natural Language Processing
    - 🔍 **Project Explain**: Developed a classification of patents using different machine learning algorithms such as Random Forest, BI-LSTM, and CNN in Python
    - 💸 **Project Tipax**: Created a website that calculates the amount of tips for a given bill using JavaScript, Express server, and HTML
    - 🎮 **Project Takuzu**: Developed the game of Takuzu using C language
    """)

    st.divider()
    
    # Section 5: Some plots
    st.header("Some plots to visualize my CV")
        
    # Languages plot
    languages = ['French', 'English', 'Spanish', 'Italian']
    scores = [10,9, 5, 2]  

    fig = go.Figure(data=[
    go.Bar(name='Proficiency', x=languages, y=scores, 
           marker_color=['#4CAF50' if score >= 8 else '#FF9800' if score >= 5 else '#F44336' for score in scores])
    ])
    
    
    fig.update_layout(
        xaxis_title='Languages',
        yaxis_title='Proficiency Level (1-10)',
        yaxis=dict(tickmode='linear', tick0=0, dtick=1),
        template='plotly_white'
    )
    
    st.title("Languages Proficiency Visualization")
    st.plotly_chart(fig)


    # Programming languages plot
    languages = ['Python', 'Java', 'C', 'HTML', 'SQL']
    scores = [9, 7, 5, 7, 8]  
       
    fig = go.Figure(data=[
    go.Bar(name='Proficiency', x=languages, y=scores, 
           marker_color=['#4CAF50' if score >= 8 else '#FF9800' if score >= 5 else '#F44336' for score in scores])
    ])
    
    
    fig.update_layout(
        xaxis_title='Programming Languages',
        yaxis_title='Proficiency Level (1-10)',
        yaxis=dict(tickmode='linear', tick0=0, dtick=1),
        template='plotly_white'
    )
    
    st.title("Programming Languages Proficiency Visualization")
    st.plotly_chart(fig)
    
    
    st.divider()
    
    # Section 6 : Contact
    st.header("Contact me 📬")
    st.markdown("""

    - 📧 **Email** : (nicolas.dupont@efrei.net)
    - 🐦 **Github* : (https://github.com/Nicolas148)
    - 💼 **LinkedIn** : (https://www.linkedin.com/in/nicolas-dupont-bb8128222/)
    """)
    
    # CV
    with open("CV .pdf", "rb") as file:
        btn = st.download_button(label="📄 Download My CV", data=file, file_name="CV .pdf", mime="application/pdf")


# Page 1
elif page == "Data Visualization":
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📊 Data Visualization </h1>", unsafe_allow_html=True)
    st.snow()
    st.write("This page is dedicated to the study of students in highschool based on their level, language 1 and 2")
  
    data = pd.read_csv("bdd_project.csv", delimiter=";")
    print(data.head)   
        

    st.header("Basic Information")
    st.write("Number of rows and columns:", data.shape)
        
      
    st.header("Data Types and Missing Values")
    st.write(data.dtypes)
    st.write("Missing values per column:")
    st.write(data.isnull().sum())
        
      
    st.header("Descriptive Statistics")
    st.write(data.describe())
    
    st.divider()
    
    st.header("Static Plots")
    
    # Box plot
    st.header("Box plots of students in Terminale G in different academies")
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Académie', y='Terminales G', data=data)
    plt.xticks(rotation=90)
    plt.title('Distribution of students in Terminales Générale Across Different Academies')
    plt.tight_layout()
    st.pyplot(plt)

    # Scatter plot
    st.header("Scatter plot of the number of students in T STI2D")
    
    plt.figure(figsize=(12,8))
    sns.scatterplot(x='Académie', y='Terminales STI2D', hue='Région académique', data=data)
    plt.title('Number of Students in Terminales STI2D by Académie and Région académique')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    st.pyplot(plt)

    # Scatter plot 2
    st.header("Scatter plot of the number of students in Terminale G")
    
    plt.figure(figsize=(12,8))
    sns.scatterplot(x='Académie', y='Terminales G', hue='Région académique', data=data)
    plt.title('Number of Students in Terminales G by Académie and Academic region')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    st.pyplot(plt)
    


    # Plot   
    st.header("Distribution of students by first and second languages")
    
    lv1_columns = ['Terminales G LV1 allemand', 'Terminales G LV1 anglais', 'Terminales G LV1 espagnol', 'Terminales G LV1 autres langues']
    lv1_data = data[lv1_columns].sum()
    
    plt.figure(figsize=(8, 5))
    lv1_data.plot(kind='bar', color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
    plt.title('Distribution of sudents by LV1 (Terminales G)')
    plt.xlabel('Langue vivante 1')
    plt.ylabel('Nombre d\'élèves')
    st.pyplot(plt)
    
    
    lv2_columns = ['Terminales G LV2 allemand', 'Terminales G LV2 anglais', 'Terminales G LV2 espagnol', 'Terminales G LV2 italien', 'Terminales G LV2 autres langues']
    lv2_data = data[lv2_columns].sum()
    
    plt.figure(figsize=(8, 5))
    lv2_data.plot(kind='bar', color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700'])
    plt.title('Distribution of students by LV2 (Terminales G)')
    plt.xlabel('Langue vivante 2')
    plt.ylabel('Nombre d\'élèves')
    st.pyplot(plt)
    
    
    # Histogram
    st.header("Histogram of the distribution of students by department")
    
    plt.figure(figsize=(12, 6))
    departement_counts = data['Département'].value_counts()
    departement_counts.plot(kind='bar', color='skyblue')
    
    plt.title('Distribution of students by department')
    plt.xlabel('Département')
    plt.ylabel('Nombre d\'élèves')
    
    plt.xticks(ticks=range(0, len(departement_counts), 10), labels=departement_counts.index[::10], rotation=90)

    st.pyplot(plt)
    
    # Heatmap 
    st.header("Heat map of the correlation between the terminales and the languages")
    
    columns = [
        'Terminales G', 'Terminales STI2D', 'Terminales STMG',
        'Terminales G LV1 allemand', 'Terminales G LV1 anglais', 'Terminales G LV1 espagnol',
        'Terminales G LV2 allemand', 'Terminales G LV2 anglais', 'Terminales G LV2 espagnol'
    ]
    corr = data[columns].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlations between terminales and languages')
    
    st.pyplot(plt)

    st.divider()
    
    st.header("Dynamic Plots")
    
    with st.expander("Click to see more"):
        st.write("Here is some more information...")
        
        # Pie chart
        sex_distribution = {
            'Girls Terminale': data['Terminales G filles'].sum(),  
            'Boys Terminale': data['Terminales G garçons'].sum(), 
            'Girls 1ère': data['1ères G filles'].sum(),  
            'Boys 1ère': data['1ères G garçons'].sum(),
            'Girls 2nde': data['2ndes GT filles'].sum(),  
            'Boys 2nde': data['2ndes GT garçons'].sum()   
        }
        
        fig = px.pie(values=sex_distribution.values(), names=sex_distribution.keys(), 
                     title="Sex Distribution of Students in Terminale, Première, and Seconde")
        
        st.title("Sex Distribution of Students")
        st.plotly_chart(fig)
           
        
        # Distribution by LV1 for the different terminales
        lv1_data = data.groupby('Académie')[['Terminales G LV1 allemand', 'Terminales G LV1 anglais', 'Terminales G LV1 espagnol']].sum().reset_index()
        
        
        fig = px.bar(lv1_data, x='Académie', y=['Terminales G LV1 allemand', 'Terminales G LV1 anglais', 'Terminales G LV1 espagnol'],
                     title='Distribution by LV1 for the different terminales', labels={'value': 'Nombre d\'élèves', 'variable': 'Langues vivantes'})
        
        st.plotly_chart(fig)
            
        # Distribution by academies for terminales
        terminales_data = data.groupby('Académie')[['Terminales G', 'Terminales STI2D', 'Terminales STMG']].sum().reset_index()
        
        fig = px.histogram(terminales_data, x='Académie', y=['Terminales G', 'Terminales STI2D', 'Terminales STMG'],
                           title='Distribution by academies for terminales',
                           labels={'value': 'Nombre d\'élèves', 'variable': 'Sections terminales'})
        
    
        st.plotly_chart(fig)
    
    st.divider()
    
    st.header("Conclusion")
    st.markdown("""
    Thanks to all these graphs, we can see the distribution of the students in different terminales and the distribution of terminales in France. To summarize, the most part of students are in Terminale Générale and have as lvl 1 : English and Lv2 : Spanish. It's pretty balanced between boys and girls throughout the years.
    """)
