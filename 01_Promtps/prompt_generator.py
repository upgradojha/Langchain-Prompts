from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""You are a marketing copywriter.
Write a short product description for:
- Product: {product_name}
- Target audience: {target_audience}
- Key features: {key_features}
Keep it under 50 words and make it engaging.""",
    input_variables=['product_name', 'target_audience', 'key_features']
)

template.save("template.json")
