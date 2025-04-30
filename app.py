import pandasai as pai

from pandasai_openai import OpenAI


llm = OpenAI(api_token="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")


pai.config.set({"llm": llm})


df_agents = pai.load('fgmm/agents')
df_invoices = pai.load('fgmm/invoices')
df_invoice_details = pai.load('fgmm/invoice-details')
df_products = pai.load('fgmm/products')
df_vans = pai.load('fgmm/vans')