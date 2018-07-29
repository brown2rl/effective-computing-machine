Name: hello_world
Version: 1
Release: 3%{?dist}
Summary: A hello world program for an arbitrary Fedora 28 package
License:  GPLv2 or BSD
URL: marketing-page.com
Source0: hello_world
# Patch0: one.patch, two.patch, three.patch
BuildArch: noarch
# BuildRequires: package1, package2 >= 2
# Requires: package1, package2
#% %prep
#%%autosetup -n #%%{name}

#% %build
# cp -R #%%{_builddir} #%%{buildroot}

%description
A hello world program for an arbitrary Fedora 28 package.

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%check



%files
%{_bindir}/hello_world

%changelog
* Sun Jul 29 2018 Mr Brown <b@a.com> 1-3
- Amended hello_world.spec 10x what a linting nightmare.
