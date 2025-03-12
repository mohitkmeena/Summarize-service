from flask import Flask, request, jsonify
import mysql.connector
import os
from dotenv import load_dotenv,dotenv_values
from mistralai.client import MistralClient


class LLMService:
    load_dotenv()
    def __init__(self):
       
        self.DB_CONFIG = {
            "host": os.getenv("MYSQL_HOST","localhost"),
            "user": os.getenv("MYSQL_USER","root"),
            "password": os.getenv("MYSQL_PASSWORD","root"),
            "database": os.getenv("MYSQL_DATABASE","blogdb"),
        }
        
        
        self.MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

        if not self.MISTRAL_API_KEY:
            raise ValueError("MISTRAL_API_KEY is not set! Please export it as an environment variable.")

        self.client = MistralClient(api_key=self.MISTRAL_API_KEY)

    def get_blog_content(self, blog_id):
        """Fetch blog content from MySQL database using a string ID."""
        conn = None
        try:
            conn = mysql.connector.connect(**self.DB_CONFIG)
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT title, content FROM blog WHERE id = %s", (blog_id,))
            blog = cursor.fetchone()

            return blog

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return None

        finally:
            if conn:
                conn.close()

    def summarize_text(self, text):
        """Use Mistral AI to summarize blog content."""
    
        response = self.client.chat(
                model="mistral-large-latest",
                messages=[{"role": "user", "content": f"Summarize this: {text}"}]
            )
        return response.choices[0].message.content

       
