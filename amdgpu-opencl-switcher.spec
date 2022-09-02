Name:          amdgpu-opencl-switcher
Version:       1.0
Release:       0%{?dist}
License:       GPL
Group:         Unspecified
Summary:       Select needed OpenCL implementation with cl_pro prefix


URL:           https://github.com/CosmicFusion/amdgpu-opencl-switcher






Provides:      amdgpu-opencl-switcher = 1.1-0.fc36
Provides:      amdgpu-opencl-switcher(x86-64) = 1.1-0.fc36
Requires:      /usr/bin/bash

%install
tar -xf amdgpu-opencl-switcher-1.0-0.f36.x86_64.tar.gz
mv usr %{buildroot}/

%description
Select needed opencl implementation with cl_pro prefix
%files
%attr(0755, root, root) "/usr/bin/cl_pro"
%attr(0644, root, root) "/usr/share/bash-completion/completions/cl_pro"

