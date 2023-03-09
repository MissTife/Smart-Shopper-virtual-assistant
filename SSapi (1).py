#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[2]:


import smart_shopper_assistant (1)


# In[3]:


from flask import Flask,request,jsonify


# In[4]:


app=Flask(__name__)

@app.route('/run_lady',methods=['GET'])
def run_lady():
    data=request.json
    result=smart_shopper_assistant (1).run_lady()
    return result

@app.route('/greet',methods=['GET'])
def greet():
    data=request.json
    result=smart_shopper_assistant.greet()
    return result

@app.route('/speak_audio',methods=['POST'])                   
def speak(audio):
    data=request.json
    result=smart_shopper_assistant.speak(audio)
    return jsonify(result)

@app.route('/takeCommand',methods=['POST'])                   
def takeCommand():
    data=request.json
    result=smart_shopper_assistant.takeCommand()
    return jsonify(result)

@app.route('/username',methods=['GET'])                   
def username():
    data=request.json
    result=smart_shopper_assistant.username()
    return result



if __name__=='__main__':
    app.run()


# In[ ]:




