from shiny import ui


def get_dashboard_ui() -> ui.Tag:
    return ui.page_fillable(
    ui.panel_title("Hello Shiny Chat"),
    ui.chat_ui("chat"),  
    fillable_mobile=True,
)
