function varargout = info_stappenteller(varargin)
% INFO_STAPPENTELLER MATLAB code for info_stappenteller.fig
%      INFO_STAPPENTELLER, by itself, creates a new INFO_STAPPENTELLER or raises the existing
%      singleton*.
%
%      H = INFO_STAPPENTELLER returns the handle to a new INFO_STAPPENTELLER or the handle to
%      the existing singleton*.
%
%      INFO_STAPPENTELLER('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in INFO_STAPPENTELLER.M with the given input arguments.
%
%      INFO_STAPPENTELLER('Property','Value',...) creates a new INFO_STAPPENTELLER or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before info_stappenteller_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to info_stappenteller_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help info_stappenteller

% Last Modified by GUIDE v2.5 24-Oct-2016 16:35:48

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @info_stappenteller_OpeningFcn, ...
                   'gui_OutputFcn',  @info_stappenteller_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before info_stappenteller is made visible.
function info_stappenteller_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to info_stappenteller (see VARARGIN)

% Choose default command line output for info_stappenteller
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes info_stappenteller wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = info_stappenteller_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

h = findobj('Tag', 'GUI');
if ~isempty(h)
    gwdata = guidata(h);
    lijst_stappen = getappdata(gwdata.help_stappenteller,'lijst_stappen')
    
    laatste_stap = lijst_stappen(end)
    m = 1;
    n = laatste_stap;
    i = repmat(1,1,length(lijst_stappen))';
    j = lijst_stappen';
    v = linspace(1,length(lijst_stappen),length(lijst_stappen))';
    new_list = sparse(i,j,v,m,n);
    
    for element = 2:laatste_stap
        if new_list(element) == 0
            new_list(element) = new_list(element-1);
        end
    end
    
    % 128 samples / seconde
    t = linspace(1,laatste_stap,laatste_stap);
    plot(t,new_list);
end







% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject, 'Value')
    close
end
