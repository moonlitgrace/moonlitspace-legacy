from django import template

register = template.Library()


@register.filter
def breadcrumb_path(path: str):
    # eg path: /blog/all
    segments = path.strip("/").split("/")
    breadcrumbs = []
    url = ""

    for segment in segments:
        url += f"/{segment}"
        breadcrumbs.append({"name": segment, "url": url})

    return breadcrumbs
