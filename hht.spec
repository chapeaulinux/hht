Summary:        A hardware inspection and graphics driver management tool
Name:           hht
Version:        0.1
Release:        1
License:        MIT
URL:            https://chapeaulinux.org
Source:         %{name}.tar.bz2
BuildArch:      noarch

Requires:	yad
Requires:	dnf
Requires:	chapeau-repos
Requires:	polkit

%description
The Hardware Helper Tool allows a user to inspect the hardware information of their
system and makes it easy to change graphics driver configuration for certain GPUs.

%prep
%setup -q

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/usr/share/hht
install -m 755 hht $RPM_BUILD_ROOT/usr/bin/
install -m 755 hht.conf $RPM_BUILD_ROOT/etc/
install -m 644 hht_left_banner.png $RPM_BUILD_ROOT/usr/share/hht/

%files
%defattr(-,root,root,-)
%dir /usr/share/hht
%config /etc/hht.conf
/usr/bin/hht

%changelog
* Sat Oct 31 2015 Vince Pooley <vince@chapeaulinux.org>
- Initial release of Hardware Helper Tool


