#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
#

Name:       kdeconnect-sfos

# >> macros
# << macros

Summary:    KDEConnect client for Sailfish
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  kdeconnect-sfos.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qt5-qtquickcontrols-layouts
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(nemonotifications-qt5)
BuildRequires:  pkgconfig(qca2-qt5) >= 2.0.0
BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= 5.31.0
BuildRequires:  kcoreaddons-devel >= 5.31.0
BuildRequires:  kdbusaddons-devel >= 5.31.0
BuildRequires:  ki18n-devel >= 5.31.0
BuildRequires:  kconfig-devel >= 5.31.0
BuildRequires:  kiconthemes-devel >= 5.31.0

%description
Short description of my Sailfish OS Application


%prep
%setup -q

# >> setup
# << setup

%build
# >> build pre
# << build pre
mkdir -p build
cd build
%cmake  .. -DSAILFISHOS=YES
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
pushd build
%make_install
popd


# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_libdir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
/etc/xdg/autostart/kdeconnectd.desktop
/usr/share/dbus-1/services/org.kde.kdeconnect.service
/usr/share/knotifications5/kdeconnect.notifyrc
/usr/share/kservicetypes5/kdeconnect_plugin.desktop
#%{_datadir}/icons/hicolor/*/apps/%{name}.png
/usr/share/icons/
# >> files
# << files