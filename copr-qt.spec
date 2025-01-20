Name:		copr-qt
Version:	0.0.1
Release:	2
Summary:	python3-copr_pyside6 launcher
Group:		Applications/Engineering
License:	GPL-3
Source1:        favicon.ico
BuildArch:	noarch
Requires:       python3dist(copr-pyside6)

%description
copr-gui provides an launcher for python3-copr-wxpython.

%global _desktopdir %{_datadir}/applications
%global _iconsdir %{_datadir}/icons

%prep

%build
cat << 'EOF' > main.py
#!/usr/bin/python3
from copr_gui.generic.pyside6 import launcher
launcher.main(default_icon='%{_iconsdir}/copr.ico')
EOF

cat << 'EOF' > copr.desktop
[Desktop Entry]
Encoding=UTF-8
Version=%{version}
Type=Application
Terminal=false
Exec=%{_bindir}/copr-qt
Name=COPR Manager
Icon=%{_iconsdir}/copr_qt.ico
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 main.py %{buildroot}%{_bindir}/copr-qt
install -Dm644 %{SOURCE1} %{buildroot}%{_iconsdir}/copr_qt.ico
install -Dm644 copr.desktop %{buildroot}%{_desktopdir}/copr_qt.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/copr-qt
%{_iconsdir}/copr_qt.ico
%{_desktopdir}/copr_qt.desktop
%changelog
