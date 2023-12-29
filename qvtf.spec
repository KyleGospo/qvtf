Name:       qvtf
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    Load Valve Texture Format files in Qt4 applications.

License:    LGPLv2.1
URL:        https://github.com/panzi/pixbufloader-vtf
VCS:        {{{ git_dir_vcs }}}
Source:     {{{ git_dir_pack }}}

Requires:   VTFLib

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: g++
BuildRequires: kdelibs-devel
BuildRequires: extra-cmake-modules
BuildRequires: shared-mime-info
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools
Buildrequires: VTFLib-devel
BuildRequires: pkgconfig(VTFLib)

# Disable debug packages
%define debug_package %{nil}

%description
QImageIO plugin to load Valve Texture Files (read-only). Using this you will be able to view VTF files in Qt programs like Gwenview.

%prep
{{{ git_dir_setup_macro }}}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license LGPL.txt
%doc README.md
%{_libdir}/qt5/plugins/imageformats/libqvtf.so
%{_datadir}/kservices5/qimageioplugins/vtf.desktop
%{_datadir}/kservices5/vtfthumbnail.desktop
