PREFIX = /usr/local

all:
	@echo Run \'make install\' to install this program!.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p main.sh $(DESTDIR)$(PREFIX)/bin/ajpm
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/jdpkg


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/jdpkg