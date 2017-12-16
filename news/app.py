
class Files(obj):



files = Files()

@app.route('/')
def index():
    title_list = files.get_file_list()
    return render_template('index.html',title_list = title_list)

@app.route('files/<filename>')
def file(filename):
    file_content = files.get_each_content(filename)
    if not file_content:
        abort(404)
    return render_template('file.html', file_item = file_content)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
