from genshi.template import TemplateLoader


def render_genshi_template_to_xhtml(template_file, context, minify=False):
    tmpl = loader.load(template_file)
    stream = tmpl.generate(context=context)
    xhtml = stream.render("xhtml")
    return html
