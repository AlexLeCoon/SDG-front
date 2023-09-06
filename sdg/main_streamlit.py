import streamlit as st
import requests
import pandas as pd
from pdfquery import PDFQuery
from collections import Counter

st.set_page_config(page_title="App page",page_icon=":recycle:")

st.sidebar.success("SDG Project")

width = 270

#dico = {15:"https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7MDLuoSaJjS-q5tZ_vJbVA.png",
        #1:"https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9KeYUomO4E0EqXT24XUypQ.png",
        #2:"https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-02.png",
        #3:"https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bD6Q8IDG3Ef444SAOnNiyg.png",
        #4:"https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1-A2Y3EWTX6V8ISs7zgU_Q.png",
        #5:"https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-05.png",
        #6:"https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-06.png",
        #7:"https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-07.png",
        #8:"https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-08.png",
        #}

col1,col2,col3 = st.columns(3)
with col2:
    st.markdown("# SDG Classifier")
with col1:
    st.image("https://www.nicepng.com/png/full/139-1391810_sdg-logo-transparent-eng-invest-sustainable-development-goals.png",width=120)
with col3:
    st.image("https://www.nicepng.com/png/full/139-1391810_sdg-logo-transparent-eng-invest-sustainable-development-goals.png",width=120)
st.header("",divider = "rainbow")
st.markdown("## PDF :open_file_folder:")

with st.form(key='params_for_api_pdf'):
    uploaded_file = st.file_uploader("Choose a file", type= 'pdf')
    if st.form_submit_button('3 SDGs & Proba'):
        if uploaded_file is not None:
            pdf=PDFQuery(uploaded_file)
            pdf.load()
            text_elements=pdf.pq("LTTextLineHorizontal")
            text=[t.text for t in text_elements]
            text = " ".join(text)
            params = {'text':text}
            sdg_classifier_api_url2 = f"https://sdgclassifier-bw4yive63a-od.a.run.app/predict_proba?{text}"
            response = requests.get(sdg_classifier_api_url2,params=params)
            prediction = response.json()
            prediction={key[:-1]+str(int(key[-1])+1):round(proba,3) for key,proba in prediction.items()}
            k = Counter(prediction)
            high = k.most_common(3)
            for i in high:
                st.markdown(f"### {i[0]} :{round(i[1],2)*100}%")
                if int(i[0][-2:]) == 5:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-05.png",width=width)
                if int(i[0][-2:]) == 1:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9KeYUomO4E0EqXT24XUypQ.png",width=width)
                if int(i[0][-2:]) == 2:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-02.png",width=width)
                if int(i[0][-2:]) == 3:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bD6Q8IDG3Ef444SAOnNiyg.png",width=width)
                if int(i[0][-2:]) == 4:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1-A2Y3EWTX6V8ISs7zgU_Q.png",width=width)
                if int(i[0][-2:]) == 6:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-06.png",width=width)
                if int(i[0][-2:]) == 7:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-07.png",width=width)
                if int(i[0][-2:]) == 8:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-08.png",width=width)
                if int(i[0][-2:]) == 9:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-09.png",width=width)
                if  int(i[0][-2:]) == 10:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-10.png",width=width)
                if  int(i[0][-2:]) == 11:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-11.png",width=width)
                if  int(i[0][-2:]) == 12:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-12.png",width=width)
                if  int(i[0][-2:]) == 13:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-13.png",width=width)
                if  int(i[0][-2:]) == 14:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-14.png",width=width)
                if  int(i[0][-2:]) == 15:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7MDLuoSaJjS-q5tZ_vJbVA.png",width=width)
                if  int(i[0][-2:]) == 16:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-16.png",width=width)

    elif st.form_submit_button("SDG"):
        if uploaded_file is not None:
            pdf=PDFQuery(uploaded_file)
            pdf.load()
            text_elements=pdf.pq("LTTextLineHorizontal")
            text=[t.text for t in text_elements]
            text = " ".join(text)
            params = {'text':text}
            sdg_classifier_api_url = f"https://sdgclassifier-bw4yive63a-od.a.run.app/predict"
            response = requests.get(sdg_classifier_api_url,params=params)
            prediction = response.json()
            pred = prediction['The text is talking about SDG:']
            st.header(f'This text should be classified in SDG {round(pred)}')

            if round(pred) == 15:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7MDLuoSaJjS-q5tZ_vJbVA.png",width=width)

            elif round(pred) == 1:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9KeYUomO4E0EqXT24XUypQ.png",width=width)

            elif round(pred) == 2:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-02.png",width=width)

            elif round(pred) == 3:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bD6Q8IDG3Ef444SAOnNiyg.png",width=width)
            elif round(pred) == 4:
                    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1-A2Y3EWTX6V8ISs7zgU_Q.png",width=width)
            elif round(pred) == 5:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-05.png",width=width)
            elif round(pred) == 6:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-06.png",width=width)
            elif round(pred) == 7:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-07.png",width=width)
            elif round(pred) == 8:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-08.png",width=width)
            elif round(pred) == 9:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-09.png",width=width)
            elif round(pred) == 10:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-10.png",width=width)
            elif round(pred) == 11:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-11.png",width=width)
            elif round(pred) == 12:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-12.png",width=width)
            elif round(pred) == 13:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-13.png",width=width)
            elif round(pred) == 14:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-14.png",width=width)
            elif round(pred) == 16:
                    st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-16.png",width=width)

    elif st.form_submit_button('Category'):
        if uploaded_file is not None:
            pdf=PDFQuery(uploaded_file)
            pdf.load()
            text_elements=pdf.pq("LTTextLineHorizontal")
            text=[t.text for t in text_elements]
            text = " ".join(text)
            params = {'text':text}
            sdg_classifier_api_url3 = f"https://sdgclassifier-bw4yive63a-od.a.run.app/predict_category?{text}"
            response = requests.get(sdg_classifier_api_url3,params=params)
            prediction = response.json()
            pred = prediction["This text most probably belongs to the following category:"]
            if pred == 1:
                results = "Economy"
            elif pred == 2:
                results = "Environement"
            else:
                results = "Societal"

        st.header(f'This text probably belongs to the category: {results}')

        if pred == 3:
            st.image("https://www.pngall.com/wp-content/uploads/9/Society-PNG-300x225.png")

        elif round(pred) == 1:
            st.image("https://www.pngall.com/wp-content/uploads/1/Save-Money-300x225.png")

        elif round(pred) == 2:
            st.image("https://www.pngall.com/wp-content/uploads/2017/05/Save-Earth-PNG-Picture.png")


st.header("",divider="rainbow")

st.markdown("## Paste an article :pencil:")

with st.form(key='params_for_api'):
    text = st.text_input("Article")
    if st.form_submit_button('3 SDGs & Proba'):
        params = dict(text=text)
        sdg_classifier_api_url2 = f"https://sdgclassifier-bw4yive63a-od.a.run.app/predict_proba?{text}"
        response = requests.get(sdg_classifier_api_url2,params=params)
        prediction = response.json()
        prediction={key[:-1]+str(int(key[-1])+1):round(proba,3) for key,proba in prediction.items()}
        k = Counter(prediction)
        high = k.most_common(3)
        for i in high:
            st.markdown(f"### {i[0]} :{round(i[1],2)*100}%")
            if int(i[0][-2:]) ==5:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-05.png",width=width)
            if int(i[0][-2:]) ==1:
                st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9KeYUomO4E0EqXT24XUypQ.png",width=width)
            if int(i[0][-2:]) ==2:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-02.png",width=width)
            if int(i[0][-2:]) ==3:
                st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bD6Q8IDG3Ef444SAOnNiyg.png",width=width)
            if int(i[0][-2:]) ==4:
                st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1-A2Y3EWTX6V8ISs7zgU_Q.png",width=width)
            if int(i[0][-2:]) ==6:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-06.png",width=width)
            if int(i[0][-2:]) ==7:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-07.png",width=width)
            if int(i[0][-2:]) ==8:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-08.png",width=width)
            if int(i[0][-2:]) ==9:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-09.png",width=width)
            if  int(i[0][-2:]) ==10:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-10.png",width=width)
            if  int(i[0][-2:]) ==11:
               st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-11.png",width=width)
            if  int(i[0][-2:]) ==12:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-12.png",width=width)
            if  int(i[0][-2:]) ==13:
                 st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-13.png",width=width)
            if  int(i[0][-2:]) ==14:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-14.png",width=width)
            if  int(i[0][-2:]) ==15:
                st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7MDLuoSaJjS-q5tZ_vJbVA.png",width=width)
            if  int(i[0][-2:]) ==16:
                st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-16.png",width=width)


    elif st.form_submit_button('SDG'):

        params = dict(text=text)
        sdg_classifier_api_url = f"https://sdgclassifier-bw4yive63a-od.a.run.app/predict?{text}"

        response = requests.get(sdg_classifier_api_url,params=params)

        prediction = response.json()

        pred = prediction['The text is talking about SDG:']

        st.header(f'This text should be classified in SDG {round(pred)}')

        if round(pred) == 15:
            st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7MDLuoSaJjS-q5tZ_vJbVA.png",width=width)

        elif round(pred) == 1:
            st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9KeYUomO4E0EqXT24XUypQ.png",width=width)

        elif round(pred) == 2:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-02.png",width=width)

        elif round(pred) == 3:
            st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bD6Q8IDG3Ef444SAOnNiyg.png",width=width)
        elif round(pred) == 4:
            st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1-A2Y3EWTX6V8ISs7zgU_Q.png",width=width)
        elif round(pred) == 5:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-05.png",width=width)
        elif round(pred) == 6:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-06.png",width=width)
        elif round(pred) == 7:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-07.png",width=width)
        elif round(pred) == 8:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-08.png",width=width)
        elif round(pred) == 9:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-09.png",width=width)
        elif round(pred) == 10:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-10.png",width=width)
        elif round(pred) == 11:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-11.png",width=width)
        elif round(pred) == 12:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-12.png",width=width)
        elif round(pred) == 13:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-13.png",width=width)
        elif round(pred) == 14:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-14.png",width=width)
        elif round(pred) == 16:
            st.image("https://www.kit.nl/wp-content/uploads/2019/02/E_SDG-goals_icons-individual-rgb-16.png",width=width)


    elif st.form_submit_button('Category'):
        params = dict(text=text)
        sdg_classifier_api_url3 = f"https://sdgclassifier-bw4yive63a-od.a.run.app/predict_category?{text}"
        response = requests.get(sdg_classifier_api_url3,params=params)
        prediction = response.json()
        pred = prediction["This text most probably belongs to the following category:"]
        if pred == 1:
            results = "Economy"
        elif pred == 2:
            results = "Environement"
        else:
            results = "Societal"

        st.header(f'This text probably belongs to the category: {results}')

        if pred == 3:
            st.image("https://www.pngall.com/wp-content/uploads/9/Society-PNG-300x225.png")

        elif round(pred) == 1:
            st.image("https://www.pngall.com/wp-content/uploads/1/Save-Money-300x225.png")

        elif round(pred) == 2:
            st.image("https://www.pngall.com/wp-content/uploads/2017/05/Save-Earth-PNG-Picture.png")
