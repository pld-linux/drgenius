Summary:	General tool for mathematics
Summary(pl):	Rozbudowane narzêdzie matematyczne
Name:		drgenius
Version:	0.5.10
Release:	6
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.5z.com/pub/genius/%{name}-%{version}.tar.gz
# Source0-md5:	17139421686934f86ed6e90e8f658532
Patch0:		%{name}-make.patch
Patch1:		%{name}-am_fix.patch
Patch2:		%{name}-gob.patch
Patch3:		%{name}-c++.patch
URL:		http://ofset.sourceforge.net/drgenius/index.html
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	gnome-libs-devel
BuildRequires:	gob >= 1.0.6
BuildRequires:	libglade-gnome-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	readline-devel >= 4.2
Obsoletes:	genius
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dr. Genius is a general tool for mathematics, including a mathematical
programming language and evaluator, an euclidian geometry tool, a
2D/3D function grapher and a console calculator. The console
calculator handles multiple precision floating point numbers, infinite
precision integers, complex numbers and matrixes.

%description -l pl
Dr. Genius to narzêdzie do rozwi±zywania problemów matematycznych.
Zawiera ono matematyczny jêzyk programowania, narzêdzie do geometrii
euklidesowej, narzêdzie do generowania wykresów 2D/3D oraz konsolowy
kalkulator. Kalkulator obs³uguje liczby zmiennoprzecinkowe wysokiej
precyzji, liczby ca³kowite, zespolone oraz macierze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# only one, broken line here
echo > exemples/macro/Makefile.am
# force regeneration, included versions have broken cpp directives
rm -f gobobjs/*.[ch]*

echo 'Categories=Math;' >> drgenius.desktop
echo 'Categories=Math;' >> genius/gnome-genius.desktop

%build
rm -f acinclude.m4
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-gnome \
	--disable-static \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_desktopdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %dir %{_libdir}/genius
%attr(755,root,root) %{_libdir}/genius/*
%{_includedir}/genius
%{_datadir}/drgenius
%{_datadir}/genius
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
