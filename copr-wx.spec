Name:		copr-wx
Version:	0.0.2
Release:	2
Summary:	python3-copr_wxpython launcher
Group:		Applications/Engineering
License:	GPL-3
Source1:        favicon.ico
BuildArch:	noarch
Requires:       python3dist(copr-wxpython)

%description
copr-gui provides an launcher for python3-copr-wxpython.

%global _desktopdir %{_datadir}/applications
%global _iconsdir %{_datadir}/icons

%prep

%build
cat << 'EOF' > main.py
#!/usr/bin/python3
from copr_gui.generic.wxpython import launcher
launcher.main(default_icon='%{_iconsdir}/copr_wx.ico')
EOF

cat << 'EOF' > copr.desktop
[Desktop Entry]
Encoding=UTF-8
Version=%{version}
Type=Application
Terminal=false
Exec=%{_bindir}/copr-wx
Name=COPR Manager
Icon=%{_iconsdir}/copr_wx.ico
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 main.py %{buildroot}%{_bindir}/copr-wx
install -Dm644 %{SOURCE1} %{buildroot}%{_iconsdir}/copr_wx.ico
install -Dm644 copr.desktop %{buildroot}%{_desktopdir}/copr_wx.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/copr-wx
%{_iconsdir}/copr_wx.ico
%{_desktopdir}/copr_wx.desktop
%changelog
