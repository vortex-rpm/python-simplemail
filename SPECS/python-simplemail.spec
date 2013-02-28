%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname simplemail

Name:           python-%{srcname}
Version:        0.3
Release:        1.vortex%{?dist}
Summary:        An easy way to send emails in Python
Vendor:         Vortex RPM

Group:          Development/Libraries
License:        MIT
URL:            https://github.com/thesharp/simplemail
Source0:        http://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-setuptools

%description
simplemail is an easy way to send emails in Python. It will use a sendmail
binary which is almost always available and ready to go.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{python_sitelib}/%{srcname}*

%changelog
* Thu Feb 28 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.3-1.vortex
- Initial packaging.

