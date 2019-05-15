FROM python:3.7.3-alpine3.9

# Install pelican plugins via subversion
RUN \
        apk update && \
        apk add subversion && \
        # -r14 is ad7c9879147bf82dc8c66e50ef464ecec4c8972c
        svn export -r14 https://github.com/akhayyat/pelican-page-hierarchy.git/trunk /usr/src/pelican-plugins/pelican-page-hierarchy && \
        # -r1436 is dc39e9af88d3c79c43495fd872ae0ad8d985337c
        svn export -r1436 https://github.com/getpelican/pelican-plugins.git/trunk/assets /usr/src/pelican-plugins/assets && \
        svn export -r1436 https://github.com/getpelican/pelican-plugins.git/trunk/neighbors /usr/src/pelican-plugins/neighbors && \
        svn export -r1436 https://github.com/getpelican/pelican-plugins.git/trunk/section_number /usr/src/pelican-plugins/section_number && \
        svn export -r1436 https://github.com/getpelican/pelican-plugins.git/trunk/tipue_search /usr/src/pelican-plugins/tipue_search && \
        # -r37 is b98d89b2cfa857c59b647ef0983a470408d6d8cd
        svn export -r37 https://github.com/ingwinlu/pelican-toc.git/trunk /usr/src/pelican-plugins/pelican_toc && \
        apk del subversion && \
        rm -rf /var/cache/apk/*

# Install pelican and related packages
RUN \
        pip install --no-cache-dir \
        pelican==4.0.1 \
        beautifulsoup4==4.7.1 \
        cssmin==0.2.0 \
        Markdown==3.1 \
        mdx_truly_sane_lists==1.2 \
        pymdown-extensions==6.0 \
        typogrify==2.0.7 \
        webassets==0.12.1

# Install theme
COPY . /usr/src/theme

# Set up default env vars
ENV \
        PELICAN_CONTENT=/usr/content \
        PELICAN_OUTPUT_PATH=/usr/build \
        PELICAN_PLUGIN_PATHS=/usr/src/pelican-plugins \
        PELICAN_THEME=/usr/src/theme \
        PELICAN_PEPYS_CACHES_PATH=/usr/caches \
        PELICAN_PEPYS_MINIFY_CSS=yes

# By default, just run pelican vs the built-in configuration
CMD pelican -s /usr/src/theme/pelicanconf.py
