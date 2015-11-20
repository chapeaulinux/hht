Summary:        A simple hardware inspection and driver management tool
Name:           hht
Version:        0.1
Release:        2
License:        MIT
URL:            https://chapeaulinux.org
Source:         %{name}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

Requires:	yad
Requires:	dnf
Requires:	chapeau-repos
Requires:	polkit

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
install -p hht.desktop %{buildroot}/usr/share/applications
install -p hht.conf %{buildroot}/etc
install -p hht_left_banner.png %{buildroot}/usr/share/hht/

%post
test -f %{_datadir}/applications/driver_helper.desktop && rm -f %{_datadir}/applications/driver_helper.desktop

%files
%config %attr(775, root, root) /etc/hht.conf
%attr(775, root, root) /usr/bin/hht
%attr(644, root, root) /usr/share/hht/hht_left_banner.png
%attr(644, root, root) /usr/share/applications/hht.desktop

%changelog
* Sat Oct 31 2015 Vince Pooley <vince@chapeaulinux.org>
- Initial release of Hardware Helper Tool


