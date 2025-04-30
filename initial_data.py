import pandasai as pai

connection = {
    "host": "127.0.0.1",
    "port": "5432",
    "user": "postgres",
    "password": "APP!@#123",
    "database": "fgmm2",
}

agents = pai.create(
    path="fgmm/agents",
    description="Agents table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "agents",
        "columns": [
            {
                "name": "id",
                "type": "integer",
                "description": "Primary key ID of the agent",
            },
            {
                "name": "en_name",
                "type": "string",
                "description": "Agent's name in English",
            },
            {
                "name": "ar_name",
                "type": "string",
                "description": "Agent's name in Arabic",
            },
            {
                "name": "mobile_1",
                "type": "string",
                "description": "Primary mobile number",
            },
            {
                "name": "mobile_2",
                "type": "string",
                "description": "Secondary mobile number",
            },
            {
                "name": "email",
                "type": "string",
                "description": "Email address of the agent",
            },
            {
                "name": "status",
                "type": "boolean",
                "description": "Whether the agent is active",
            },
            {
                "name": "type",
                "type": "string",
                "description": "Type of agent (e.g., distributor, retailer)",
            },
            {
                "name": "center_id",
                "type": "integer",
                "description": "ID of the agent's center",
            },
            {"name": "created_at", "type": "timestamp", "description": "Creation date"},
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Last update date",
            },
        ],
    },
)

vans = pai.create(
    path="fgmm/vans",
    description="Vans table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "vans",
        "columns": [
            {
                "name": "id",
                "type": "integer",
                "description": "Primary key ID of the van",
            },
            {"name": "name", "type": "string", "description": "Name of the van driver"},
            {
                "name": "van_size",
                "type": "string",
                "description": "Size category of the van",
            },
            {"name": "email", "type": "string", "description": "Email address"},
            {"name": "car_type", "type": "string", "description": "Type of the car"},
            {
                "name": "van_type",
                "type": "string",
                "description": "Type of van (e.g., freezer, dry)",
            },
            {
                "name": "status",
                "type": "boolean",
                "description": "Whether the van is active",
            },
            {"name": "created_at", "type": "timestamp", "description": "Creation date"},
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Last update date",
            },
        ],
    },
)

products = pai.create(
    path="fgmm/products",
    description="Products table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "products",
        "columns": [
            {"name": "id", "type": "integer", "description": "Product ID"},
            {
                "name": "en_name",
                "type": "string",
                "description": "Product name in English",
            },
            {
                "name": "ar_name",
                "type": "string",
                "description": "Product name in Arabic",
            },
            {"name": "item_code", "type": "string", "description": "Item code or SKU"},
            {
                "name": "category_id",
                "type": "integer",
                "description": "Main category ID",
            },
            {
                "name": "subcategory_id",
                "type": "integer",
                "description": "Subcategory ID",
            },
            {
                "name": "unit_id",
                "type": "integer",
                "description": "Measurement unit ID",
            },
            {
                "name": "cost_price",
                "type": "float",
                "description": "Product cost price",
            },
            {
                "name": "sale_price",
                "type": "float",
                "description": "Product sale price",
            },
            {
                "name": "vat_value",
                "type": "float",
                "description": "VAT value for the product",
            },
            {"name": "created_at", "type": "timestamp", "description": "Creation date"},
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Last update date",
            },
        ],
    },
)

invoices = pai.create(
    path="fgmm/invoices",
    description="Invoices table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "invoices",
        "columns": [
            {"name": "id", "type": "integer", "description": "Invoice ID"},
            {
                "name": "invoice_ref",
                "type": "string",
                "description": "Reference code of the invoice",
            },
            {
                "name": "seller_id",
                "type": "integer",
                "description": "ID of the seller (agent or van)",
            },
            {
                "name": "buyer_id",
                "type": "integer",
                "description": "ID of the buyer (agent or customer)",
            },
            {
                "name": "total_qty",
                "type": "integer",
                "description": "Total quantity in invoice",
            },
            {
                "name": "total_price",
                "type": "float",
                "description": "Total price of the invoice",
            },
            {"name": "vat_amount", "type": "float", "description": "VAT amount"},
            {"name": "discount", "type": "float", "description": "Discount applied"},
            {
                "name": "net_total",
                "type": "float",
                "description": "Total after discount and VAT",
            },
            {"name": "created_at", "type": "timestamp", "description": "Creation date"},
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Last update date",
            },
        ],
    },
)

invoice_detials = pai.create(
    path="fgmm/invoice-details",
    description="Invoice details table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "invoice_detials",
        "columns": [
            {"name": "id", "type": "integer", "description": "Invoice detail ID"},
            {
                "name": "invoice_id",
                "type": "integer",
                "description": "Reference to invoice",
            },
            {
                "name": "product_id",
                "type": "integer",
                "description": "Referenced product",
            },
            {"name": "quantity", "type": "integer", "description": "Quantity sold"},
            {"name": "price", "type": "float", "description": "Unit price of product"},
            {
                "name": "discount",
                "type": "float",
                "description": "Discount per line item",
            },
            {
                "name": "vat_amount",
                "type": "float",
                "description": "VAT amount for the line",
            },
            {
                "name": "total",
                "type": "float",
                "description": "Total price after discount and VAT",
            },
            {"name": "created_at", "type": "timestamp", "description": "Creation date"},
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Last update date",
            },
        ],
    },
)
