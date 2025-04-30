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
    description="Invoices table containing detailed sales transaction data",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "invoices",
        "columns": [
            {"name": "id", "type": "bigint", "description": "Primary key"},
            {
                "name": "invoice_ref",
                "type": "string",
                "description": "Reference number for the invoice",
            },
            {"name": "seller_id", "type": "integer", "description": "ID of the seller"},
            {
                "name": "seller_type",
                "type": "string",
                "description": "Type of the seller",
            },
            {"name": "buyer_id", "type": "integer", "description": "ID of the buyer"},
            {
                "name": "buyer_type",
                "type": "string",
                "description": "Type of the buyer",
            },
            {
                "name": "total_qty",
                "type": "integer",
                "description": "Total quantity of items sold",
            },
            {
                "name": "total_price",
                "type": "float",
                "description": "Total price of the invoice",
            },
            {
                "name": "description",
                "type": "string",
                "description": "Additional notes or description",
            },
            {
                "name": "status",
                "type": "boolean",
                "description": "Invoice status (active/inactive)",
            },
            {
                "name": "created_at",
                "type": "datetime",
                "description": "Timestamp of creation",
            },
            {
                "name": "updated_at",
                "type": "datetime",
                "description": "Timestamp of last update",
            },
            {
                "name": "deleted_at",
                "type": "datetime",
                "description": "Timestamp of deletion",
            },
            {
                "name": "is_sap",
                "type": "boolean",
                "description": "Indicates if invoice is synced with SAP",
            },
            {
                "name": "doc_number",
                "type": "integer",
                "description": "SAP document number",
            },
            {
                "name": "return_status",
                "type": "integer",
                "description": "Return status of the invoice",
            },
            {
                "name": "created_by",
                "type": "integer",
                "description": "User who created the invoice",
            },
            {
                "name": "createable_type",
                "type": "string",
                "description": "Creator entity type (e.g., admin)",
            },
            {
                "name": "temp_id",
                "type": "string",
                "description": "Temporary ID for internal tracking",
            },
            {
                "name": "is_gift",
                "type": "boolean",
                "description": "Indicates if invoice is a gift",
            },
            {
                "name": "sale_type",
                "type": "string",
                "description": "Type of sale (e.g., normal_sale)",
            },
            {
                "name": "sync_time",
                "type": "datetime",
                "description": "Time when invoice was synced",
            },
            {
                "name": "creation_way",
                "type": "string",
                "description": "Way the invoice was created (e.g., web)",
            },
            {
                "name": "image",
                "type": "string",
                "description": "Image or receipt of the invoice",
            },
            {"name": "doc_key", "type": "integer", "description": "SAP document key"},
            {
                "name": "is_wallet_deduct",
                "type": "integer",
                "description": "Indicates wallet deduction",
            },
            {
                "name": "is_agent_offer",
                "type": "boolean",
                "description": "Indicates use of agent offer",
            },
            {
                "name": "agency_id",
                "type": "integer",
                "description": "Related agency ID",
            },
            {"name": "brand_id", "type": "integer", "description": "Related brand ID"},
            {
                "name": "app_version",
                "type": "string",
                "description": "App version used to create invoice",
            },
            {
                "name": "customer_classification",
                "type": "boolean",
                "description": "Indicates customer classification",
            },
            {"name": "is_van_gift", "type": "boolean", "description": "Van gift flag"},
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

price_lists = pai.create(
    path="fgmm/price-lists",
    description="Price lists table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "price_lists",
        "columns": [
            {"name": "id", "type": "bigint", "description": "Primary key"},
            {
                "name": "en_name",
                "type": "string",
                "description": "English name of the price list",
            },
            {
                "name": "ar_name",
                "type": "string",
                "description": "Arabic name of the price list",
            },
            {
                "name": "created_for",
                "type": "string",
                "description": "Purpose for which the price list was created",
            },
            {
                "name": "center_id",
                "type": "integer",
                "description": "ID of the center associated with this price list",
            },
            {
                "name": "en_description",
                "type": "text",
                "description": "English description",
            },
            {
                "name": "ar_description",
                "type": "text",
                "description": "Arabic description",
            },
            {
                "name": "created_at",
                "type": "timestamp",
                "description": "Timestamp when the record was created",
            },
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Timestamp when the record was last updated",
            },
            {
                "name": "status",
                "type": "boolean",
                "description": "Status of the price list (active/inactive)",
            },
            {
                "name": "agency_id",
                "type": "integer",
                "description": "ID of the associated agency",
            },
            {
                "name": "brand_id",
                "type": "integer",
                "description": "ID of the associated brand",
            },
            {
                "name": "price_listable_id",
                "type": "integer",
                "description": "Polymorphic relation ID",
            },
            {
                "name": "price_listable_type",
                "type": "string",
                "description": "Polymorphic relation type",
            },
            {
                "name": "is_custom",
                "type": "boolean",
                "description": "Indicates if the price list is custom",
            },
            {
                "name": "is_expired",
                "type": "boolean",
                "description": "Indicates if the price list is expired",
            },
            {
                "name": "is_gift",
                "type": "integer",
                "description": "Indicates if the price list contains gifts",
            },
        ],
    },
)

price_list_items = pai.create(
    path="fgmm/price-list-items",
    description="Price list items table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "price_list_items",
        "columns": [
            {"name": "id", "type": "bigint", "description": "Primary key"},
            {
                "name": "price_list_id",
                "type": "integer",
                "description": "ID of the associated price list",
            },
            {
                "name": "product_id",
                "type": "integer",
                "description": "ID of the product",
            },
            {"name": "item_code", "type": "string", "description": "Code of the item"},
            {"name": "item_name", "type": "string", "description": "Name of the item"},
            {
                "name": "item_price",
                "type": "string",
                "description": "Price of the item",
            },
            {
                "name": "created_at",
                "type": "timestamp",
                "description": "Creation timestamp",
            },
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Update timestamp",
            },
        ],
    },
)

offers = pai.create(
    path="fgmm/offers",
    description="Offers table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "offers",
        "columns": [
            {"name": "id", "type": "bigint", "description": "Primary key"},
            {"name": "name", "type": "string", "description": "Name of the offer"},
            {"name": "type", "type": "string", "description": "Type of the offer"},
            {
                "name": "description",
                "type": "text",
                "description": "Description of the offer",
            },
            {
                "name": "deleted_at",
                "type": "timestamp",
                "description": "Timestamp for soft deletion",
            },
            {
                "name": "created_at",
                "type": "timestamp",
                "description": "Creation timestamp",
            },
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Update timestamp",
            },
            {
                "name": "start_date",
                "type": "string",
                "description": "Start date of the offer",
            },
            {
                "name": "end_date",
                "type": "string",
                "description": "End date of the offer",
            },
            {
                "name": "agency_id",
                "type": "integer",
                "description": "ID of the associated agency",
            },
            {
                "name": "brand_id",
                "type": "integer",
                "description": "ID of the associated brand",
            },
            {"name": "image", "type": "string", "description": "Image path or URL"},
            {
                "name": "status",
                "type": "boolean",
                "description": "Status of the offer (active/inactive)",
            },
            {
                "name": "offer_code",
                "type": "string",
                "description": "Code of the offer",
            },
            {
                "name": "has_bp_classification",
                "type": "integer",
                "description": "Indicates presence of BP classification",
            },
            {
                "name": "is_processed",
                "type": "boolean",
                "description": "Indicates if the offer has been processed",
            },
            {
                "name": "curve_image",
                "type": "string",
                "description": "Path or URL of the curve image",
            },
            {"name": "note", "type": "text", "description": "Additional notes"},
            {
                "name": "gift_type",
                "type": "string",
                "description": "Type of gift offered",
            },
            {
                "name": "price",
                "type": "integer",
                "description": "Price associated with the offer",
            },
        ],
    },
)

offer_product = pai.create(
    path="fgmm/offer-product",
    description="Offer product pivot table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "offer_product",
        "columns": [
            {"name": "id", "type": "integer", "description": "Primary key"},
            {
                "name": "offer_id",
                "type": "integer",
                "description": "ID of the associated offer",
            },
            {
                "name": "product_id",
                "type": "integer",
                "description": "ID of the associated product",
            },
        ],
    },
)

invoice_returns = pai.create(
    path="fgmm/invoice-returns",
    description="Invoice returns table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "invoice_returns",
        "columns": [
            {"name": "id", "type": "bigint", "description": "Primary key"},
            {
                "name": "invoice_return_ref",
                "type": "string",
                "description": "Reference code of the invoice return",
            },
            {
                "name": "invoice_id",
                "type": "integer",
                "description": "ID of the original invoice",
            },
            {"name": "seller_id", "type": "integer", "description": "ID of the seller"},
            {
                "name": "seller_type",
                "type": "string",
                "description": "Type of the seller (e.g., agency, distributor)",
            },
            {"name": "buyer_id", "type": "integer", "description": "ID of the buyer"},
            {
                "name": "buyer_type",
                "type": "string",
                "description": "Type of the buyer (e.g., customer, retailer)",
            },
            {
                "name": "total_qty",
                "type": "integer",
                "description": "Total quantity returned",
            },
            {
                "name": "total_price",
                "type": "numeric(20,6)",
                "description": "Total price of the returned items",
            },
            {
                "name": "description",
                "type": "string",
                "description": "Description or reason for the return",
            },
            {
                "name": "status",
                "type": "boolean",
                "description": "Return status (active/inactive)",
            },
            {
                "name": "created_at",
                "type": "timestamp",
                "description": "Creation timestamp",
            },
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Update timestamp",
            },
            {
                "name": "deleted_at",
                "type": "timestamp",
                "description": "Timestamp of deletion if soft-deleted",
            },
            {
                "name": "created_by",
                "type": "integer",
                "description": "ID of the creator",
            },
            {
                "name": "createable_type",
                "type": "string",
                "description": "Type of creator (e.g., admin)",
            },
            {
                "name": "temp_id",
                "type": "string",
                "description": "Temporary identifier",
            },
            {
                "name": "sync_time",
                "type": "timestamp",
                "description": "Timestamp when data was last synced",
            },
            {
                "name": "creation_way",
                "type": "string",
                "description": "Method used for creation (e.g., web)",
            },
        ],
    },
)

invoice_return_details = pai.create(
    path="fgmm/invoice-return-details",
    description="Invoice return details table",
    source={
        "type": "postgres",
        "connection": connection,
        "table": "invoice_return_details",
        "columns": [
            {"name": "id", "type": "bigint", "description": "Primary key"},
            {
                "name": "invoice_return_id",
                "type": "integer",
                "description": "ID of the related invoice return",
            },
            {
                "name": "product_id",
                "type": "integer",
                "description": "ID of the returned product",
            },
            {
                "name": "quantity",
                "type": "integer",
                "description": "Quantity of product returned",
            },
            {
                "name": "price",
                "type": "numeric(20,6)",
                "description": "Unit price of the returned item",
            },
            {
                "name": "created_at",
                "type": "timestamp",
                "description": "Creation timestamp",
            },
            {
                "name": "updated_at",
                "type": "timestamp",
                "description": "Update timestamp",
            },
            {
                "name": "deleted_at",
                "type": "timestamp",
                "description": "Timestamp of deletion if soft-deleted",
            },
        ],
    },
)
