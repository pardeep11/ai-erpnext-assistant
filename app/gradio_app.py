import gradio as gr

from app.erpnext.sales_order import SalesOrderService
from app.agents.analyzer import SalesOrderAnalyzer
from app.graph.workflow import workflow


sales_order_service = SalesOrderService()
analyzer = SalesOrderAnalyzer()


# WITHOUT REFLECTION
def analyze_without_reflection(customer):
    orders = sales_order_service.get_sales_orders()

    analysis = analyzer.analyze(
        customer=customer,
        orders=orders,
    )

    return analysis


# WITH REFLECTION
def analyze_with_reflection(customer):
    orders = sales_order_service.get_sales_orders()

    initial_state = {
        "customer": customer,
        "sales_orders": orders,
        "analysis": "",
        "reflection": "",
        "approved": False,
        "iteration": 0,
    }

    result = workflow.invoke(initial_state)

    return result["analysis"]


with gr.Blocks() as demo:

    gr.Markdown("# ERPNext AI Business Assistant")

    customer = gr.Textbox(
        label="Customer",
        placeholder="Enter customer name",
    )

    analyze_button = gr.Button("Analyze Customer")

    with gr.Row():

        with gr.Column():
            gr.Markdown("### Without Reflection")

            output_without = gr.Textbox(
                label="Analyzer Output",
                lines=25,
                max_lines=30,
            )

        with gr.Column():
            gr.Markdown("### With Reflection")

            output_with = gr.Textbox(
                label="Final Output",
                lines=25,
                max_lines=30,
            )

    analyze_button.click(
        fn=analyze_without_reflection,
        inputs=customer,
        outputs=output_without,
    )

    analyze_button.click(
        fn=analyze_with_reflection,
        inputs=customer,
        outputs=output_with,
    )


demo.launch()