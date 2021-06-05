from chatbot import Chat, register_call
import wikipedia
import os
import warnings
warnings.filterwarnings("ignore")

# for get products from amazon
from amazon.api import AmazonAPI

@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "No encuentro nada acerca de "+query

@register_call("getproduct")
def get_product(session, query):
    if query == " limon ":
        return "El precio del producto es: 18.15 Q"
    if str(query) == " leche ":
        return "El precio del producto es: 16.95 Q"
    if str(query) == " queso ":
        return "No tenemos el producto que buscas pero estos podrian interesarte: \n-pan con queso \n-queso mozzarella "
    # print(query)
    return "No tenemos ningun producto parecido a eso"


# @register_call("getprice")
# def get_price(session, query):
    
#     amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
#     products = amazon.search(Keywords='kindle', SearchIndex='All')


first_question = "Hola, Como puedo ayudarte?"
chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatbot_administracion.template"))
chat.converse(first_question)
