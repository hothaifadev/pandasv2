from typing import Union
from fastapi import FastAPI
import pandasai as pai
from pandasai_openai import OpenAI
import pandas as pd


app = FastAPI()


llm = OpenAI(
    api_token="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"
)

pai.config.set({"llm": llm})

df_agents = pai.load("fgmm/agents")
df_invoices = pai.load("fgmm/invoices")
df_invoice_details = pai.load("fgmm/invoice-details")
df_products = pai.load("fgmm/products")
df_vans = pai.load("fgmm/vans")

df_price_lists = pai.load("fgmm/price-lists")
df_price_list_items = pai.load("fgmm/price-list-items")
df_offers = pai.load("fgmm/offers")
df_offer_product = pai.load("fgmm/offer-product")
df_invoice_returns = pai.load("fgmm/invoice-returns")
df_invoice_return_details = pai.load("fgmm/invoice-return-details")


@app.get("/")
def read_root(prompt: str):
    response = pai.chat(
        prompt,
        df_agents,
        df_invoices,
        df_invoice_details,
        df_products,
        df_vans,
        df_price_lists,
        df_price_list_items,
        df_offers,
        df_offer_product,
        df_invoice_returns,
        df_invoice_return_details,
    )

    # Handle different return types
    if isinstance(response, pd.DataFrame):
        return response.to_dict(orient="records")
    elif isinstance(response, (list, dict)):
        return response
    else:
        return {"result": str(response)}
