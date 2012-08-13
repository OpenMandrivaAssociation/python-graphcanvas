%define module	graphcanvas
%define name 	python-%{module}
%define version 4.0.0
%define	rel		2
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary: 	Enthought Tool Suite - interactive graph visualization
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://github.com/enthought/graphcanvas/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires:  	python-enable >= 4.2.0
Requires:  	python-networkx
BuildRequires: 	python-setuptools >= 0.6c8

%description
graphcanvas is an library for interacting with visualizations of
complex graphs. The aim is to allow the developer to declare the graph
by the simplest means and be able to visualize the graph immediately.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc examples/ 
%py_sitedir/%{module}*
