PREFIX = /usr/local

all:
	@echo Run \'make install\' to install this program!.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p index.py $(DESTDIR)$(PREFIX)/bin/ajpm
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/ajpm


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/ajpm
	@rm -rf /etc/ajpm