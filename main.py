#Installation of ScratchAttach

import os

os.system("pip install -U scratchattach")

#Logging In With My Account xD.

import scratchattach as scratch3

session = scratch3.Session(".eJxVUMtOwzAQ_Bef2-BX8-iNSlyAcoAKlVO0djaNaWJXiaOoIP6dtdRLb6uZndmZ_WXzhKOHAdmWHfcQcX1A27EVq2GOXZ3Y2jVEVlrqsuSCqIhTtCGcXRItYTxjcy8wYM_okyph6KOzEF3w2Y2Ysne89Ddwd1sm30ADiVoJZV5wW2hhteItVBKMpeNaSGUMbvW8u3avB3yuwrI_fpqPJ14dquugX0qy6cPJ-bW7kJPYFJnmmZA8y1XK2IM_zXBKwenUijXfBIQ6ugF_gk_w44AjJXt4w6X-om73zTqYuqSttLJSKC5aoyxFzE1jeKEQOIr0Jo6woQ7s7x8_5XDm:1rruZi:iLn3iflqmq4XQe--94iIybXLetM", username="XMate-Tech") #The username field is case sensitive

#Connecting To Project "ScratchStats"
project = session.connect_project("994058692")

#Connecting with Cloud Variables of Project "ScratchStats"
conn = session.connect_cloud("994058692")

#Setting Up Variables
conn.set_var("FROM_HOST_1", project.loves) #the variable name is specified without the cloud emoji
conn.set_var("FROM_HOST_2", project.favorites)
conn.set_var("FROM_HOST_3", project.remix_count)
conn.set_var("FROM_HOST_4", project.views)
