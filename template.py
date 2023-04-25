from jinja2 import Environment, FileSystemLoader


class Template:
    def __init__(self, template_dir: str):
        self.loader = FileSystemLoader(template_dir)
        self.env = Environment(loader=self.loader)

    def load_template(self, template_name: str):
        self.template = self.env.get_template(template_name)

    def set_context(self, context: any):
        self.context = context

    def render_to_html(self):
        html = self.template.render(self.context)

        return html

    def render_to_file(self, file_name: str):
        html = self.template.render(self.context)

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html)
