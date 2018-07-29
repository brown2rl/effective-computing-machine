Name: hello_world
Version: 1
Release: 3%{?dist}
Summary: A hello world program for an arbitrary Fedora 28 package
License:  GPLv2
Source0: hello_world
BuildArch: noarch

%description
A hello world program for an arbitrary Fedora 28 package.

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/hello_world

%changelog
