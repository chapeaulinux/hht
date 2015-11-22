Summary:        A simple hardware inspection and driver management tool
Name:           hht
Version:        0.1
Release:        5
License:        MIT
URL:            https://chapeaulinux.org
Source:         %{name}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

Requires:	yad
Requires:	dnf
Requires:	chapeau-repos
Requires:	polkit
Requires:	usbutils

%description
Inspect your system's hardware information and configure third-party drivers.

%prep
%setup -q -c -n hht

%build

%install
mkdir -p %{buildroot}/usr/share/hht
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
install -p hht %{buildroot}/usr/bin
install -p hhtsu %{buildroot}/usr/bin
install -p hht.desktop %{buildroot}/usr/share/applications
install -p hht.conf %{buildroot}/etc
install -p hht_left_banner.png %{buildroot}/usr/share/hht/

%post
test -f %{_datadir}/applications/driver_helper.desktop && rm -f %{_datadir}/applications/driver_helper.desktop

%files
%config %attr(775, root, root) /etc/hht.conf
%attr(744, root, root) /usr/bin/hht
%attr(755, root, root) /usr/bin/hhtsu
%attr(644, root, root) /usr/share/hht/hht_left_banner.png
%attr(644, root, root) /usr/share/applications/hht.desktop

%changelog
* Sat Nov 21 2015 Vince Pooley <vince@chapeaulinux.org>
- Passthrough of DISPLAY variable from hhtsu to hht

* Sat Nov 21 2015 Vince Pooley <vince@chapeaulinux.org>
- Update spec changelog.
- Added requirement for usbutils package.
- Going back to dnf to manage packages as pkcon is pants, added hhtsu wrapper script to the package which runs hht as root using pkexec.
- hht.desktop amended to run hhtsu instead of hht
- Fixed GPU overview heading when GPU is "other"

* Thu Nov 19 2015 Vince Pooley <vince@chapeaulinux.org>
- Instead of specifying multiple package names, use new meta packages created for Chapeau. This works much better with pkcon.

* Sat Nov 14 2015 Vince Pooley <vince@chapeaulinux.org>
- Changed to use packagekit instead of dnf which doesn't require sudo

* Sat Nov 14 2015 Vince Pooley <vince@chapeaulinux.org>
- Changed to use packagekit instead of dnf which doesn't require sudo

* Sat Oct 31 2015 Vince Pooley <vince@chapeaulinux.org>
- Initial release of Hardware Helper Tool

