import os


def on_files(files, *, config):
    site = config.site_dir
    for file in files:
        if file.src_uri == 'introduce/homepage/index.md':
            file.url = "./"
            file.dest_uri = file.dest_uri.replace("introduce/homepage/", "")
            file.abs_dest_path = os.path.join(site, file.dest_path)
