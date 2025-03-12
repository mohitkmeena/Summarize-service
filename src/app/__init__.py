from flask import Flask,request,jsonify
import os
import json
from service.llmservice import LLMService
app=Flask(__name__)

ls=LLMService()

@app.route("/summarize/<string:blog_id>", methods=["GET"])
def summarize_blog(blog_id):
    """API Endpoint: Get summarized blog content by ID."""
    blog = ls.get_blog_content(blog_id)

    if not blog:
        return jsonify({"error": "Blog not found"}), 404

    summary = ls.summarize_text(blog["content"])

    return jsonify({
        "blog_id": blog_id,
        "title": blog["title"],
        "summary": summary
    })

if __name__ =="__main__":
    app.run(host="localhost",port=8010,debug=True)