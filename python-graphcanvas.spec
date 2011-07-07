%define module	graphcanvas
%define name 	python-%{module}
%define version 4.0.0
%define release %mkrel 1

Summary: 	Enthought Tool Suite - graphcanvas project
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://code.enthought.com/projects/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires:  	python-enable >= 4.0.0
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

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc examples/ 
