function varargout = Instellingen(varargin)
% PANEL1 MATLAB code for panel1.fig
%      PANEL1, by itself, creates a new PANEL1 or raises the existing
%      singleton*.
%
%      H = PANEL1 returns the handle to a new PANEL1 or the handle to
%      the existing singleton*.
%
%      PANEL1('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in PANEL1.M with the given input arguments.
%
%      PANEL1('Property','Value',...) creates a new PANEL1 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Instellingen_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Instellingen_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help panel1

% Last Modified by GUIDE v2.5 01-Dec-2016 16:18:58

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Instellingen_OpeningFcn, ...
                   'gui_OutputFcn',  @Instellingen_OutputFcn, ...
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


% --- Executes just before panel1 is made visible.
function Instellingen_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to panel1 (see VARARGIN)

% Choose default command line output for panel1
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes panel1 wait for user response (see UIRESUME)
% uiwait(handles.panel1);

set(gcf, 'units','normalized','outerposition',[0 0 1 1])
%set(handles.Instellingen, 'Units', 'normalized', 'OuterPosition', [0 0 1 1])

gm = findobj('Tag','GUI');
if ~isempty(gm)
    gmdata = guidata(gm);
    if get(gmdata.language_eng, 'Value')
        set(handles.Eng, 'Value', 1.0)
        Eng_Callback(handles.Eng, eventdata, handles)
    end
    if strcmp(get(gmdata.axes_ecg, 'Visible'),'off')
        set(handles.ECG, 'Value', 0.0)
    end
    if strcmp(get(gmdata.axes_ppg, 'Visible'), 'off')
        set(handles.POM, 'Value', 0.0)
    end
    if strcmp(get(gmdata.axes_stappenteller, 'Visible'), 'off')
        set(handles.stepcounter, 'Value', 0.0)
    end
end

%lay-out implementation
all_radiobuttons = findall(0, 'Style','radiobutton');
all_toggle = findall(0,'Style','togglebutton');
all_push = findall(0,'Style','pushbutton');
all_panels = findall(0,'Type','uipanel');
all_button_groups = findall(0,'Type','uibuttongroup');
all_edit = findall(0, 'Style','edit');

set(all_radiobuttons,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize', 16);

set(all_edit, 'FontSize', 16)

set(all_toggle,...
'BackgroundColor',[0.118 0.231 0.443],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

set(all_push,...
'BackgroundColor',[0.118 0.231 0.443],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

set(handles.Instellingen,...
'units', 'normalized',...
'OuterPosition', [0 0 1 1],...
'Color',[0.886 0.91 0.953]);

set(all_panels,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',18,...
'ForegroundColor',[1 1 1]);

set(all_button_groups,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',18,...
'ForegroundColor',[1 1 1]);

set(handles.text2,'BackgroundColor',[0.886 0.91 0.953],...
 'ForegroundColor', [0 0 0],...
 'FontSize',32);

set(handles.text3,'BackgroundColor',[0.886 0.91 0.953],...
 'ForegroundColor', [0 0 0],...
 'FontSize',14);

set(handles.text4,'BackgroundColor',[0.886 0.91 0.953],...
 'ForegroundColor', [0 0 0],...
 'FontSize',14);

set(handles.text7,'BackgroundColor',[0.886 0.91 0.953],...
 'ForegroundColor', [0 0 0],...
 'FontSize',14);

set(handles.text5,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

set(handles.text6,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

set(handles.text8,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);



% --- Outputs from this function are returned to the command line.
function varargout = Instellingen_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



% --- Executes on button press in ECG.
function ECG_Callback(hObject, eventdata, handles)
% hObject    handle to ECG (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of ECG
gm = findobj('Tag','GUI');
if ~isempty(gm)
    gmdata = guidata(gm);
    if get(hObject, 'Value')
        set(gmdata.text4, 'Visible', 'on')
        set(gmdata.text10, 'Visible', 'on')
        set(gmdata.text7, 'Visible', 'on')
        set(gmdata.help_ecg, 'Visible', 'on')
        set(gmdata.axes_ecg, 'Visible', 'on')
    else
        set(gmdata.text4, 'Visible', 'off')
        set(gmdata.text10, 'Visible', 'off')
        set(gmdata.text7, 'Visible', 'off')
        set(gmdata.help_ecg, 'Visible', 'off')
        set(gmdata.axes_ecg, 'Visible', 'off')
    end
end

    

% --- Executes on button press in POM.
function POM_Callback(hObject, eventdata, handles)
% hObject    handle to POM (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of POM
gm = findobj('Tag','GUI');
if ~isempty(gm)
    gmdata = guidata(gm);
    if get(hObject, 'Value')
        set(gmdata.text5, 'Visible', 'on')
        set(gmdata.text8, 'Visible', 'on')
        set(gmdata.text6, 'Visible', 'on')
        set(gmdata.help_ppg, 'Visible', 'on')
        set(gmdata.axes_ppg, 'Visible', 'on') 
    else
        set(gmdata.text5, 'Visible', 'off')
        set(gmdata.text8, 'Visible', 'off')
        set(gmdata.text6, 'Visible', 'off')
        set(gmdata.help_ppg, 'Visible', 'off')
        set(gmdata.axes_ppg, 'Visible', 'off')
    end
end

% --- Executes on button press in stepcounter.
function stepcounter_Callback(hObject, eventdata, handles)
% hObject    handle to stepcounter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of stepcounter
gm = findobj('Tag','GUI');
if ~isempty(gm)
    gmdata = guidata(gm);
    if get(hObject, 'Value')
        set(gmdata.text9, 'Visible', 'on')
        set(gmdata.goal, 'Visible', 'on')
        set(gmdata.goalnumber, 'Visible', 'on')
        set(gmdata.text14, 'Visible', 'on')
        set(gmdata.help_stappenteller, 'Visible', 'on')
        set(gmdata.axes_stappenteller, 'Visible', 'on') 
    else
        set(gmdata.text9, 'Visible', 'off')
        set(gmdata.goal, 'Visible', 'off')
        set(gmdata.goalnumber, 'Visible', 'off')
        set(gmdata.text14, 'Visible', 'off')
        set(gmdata.help_stappenteller, 'Visible', 'off')
        set(gmdata.axes_stappenteller, 'Visible', 'off')
    end
end

% --- Executes on button press in close.
function close_Callback(hObject, eventdata, handles)
% hObject    handle to close (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject, 'Value')
    if ~isempty(get(handles.goal, 'String'))
        gm = findobj('Tag','GUI');
        if ~isempty(gm)
            gmdata = guidata(gm);
            set(gmdata.goalnumber, 'String', get(handles.goal, 'String'))
        end
    end
    close
end



function email_Callback(hObject, eventdata, handles)
% hObject    handle to email (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of email as text
%        str2double(get(hObject,'String')) returns contents of email as a double



% --- Executes during object creation, after setting all properties.
function email_CreateFcn(hObject, eventdata, handles)
% hObject    handle to email (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Skype_Callback(hObject, eventdata, handles)
% hObject    handle to Skype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Skype as text
%        str2double(get(hObject,'String')) returns contents of Skype as a double


% --- Executes during object creation, after setting all properties.
function Skype_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Skype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function goal_Callback(hObject, eventdata, handles)
% hObject    handle to goal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of goal as text
%        str2double(get(hObject,'String')) returns contents of goal as a double



% --- Executes during object creation, after setting all properties.
function goal_CreateFcn(hObject, eventdata, handles)
% hObject    handle to goal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Ned.
function Ned_Callback(hObject, eventdata, handles)
% hObject    handle to Ned (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of Ned
if get(hObject, 'Value')
    set(handles.text2, 'String', 'Instellingen')
    set(handles.text3, 'String', 'In onderstaand menu kan u aanduiden welke grafieken u getoond wil hebben.')
    set(handles.panel1, 'Title', 'Grafieken')
    set(handles.stepcounter, 'String', 'Stappenteller')
    set(handles.text7, 'String', 'Dagdoel:')
    set(handles.uipanel4, 'Title', 'Stappenteller')
    set(handles.text8, 'String', 'Dagdoel')
    set(handles.text4, 'String', 'Hier kan u eventuele veranderingen van uw gegevens doorgeven.')
    set(handles.uipanel2, 'Title', 'Persoonlijke gegevens')
    set(handles.uibuttongroup1, 'Title', 'Geslacht')
    set(handles.male, 'String', 'Man')
    set(handles.female, 'String', 'Vrouw')
    set(handles.uibuttongroup2, 'Title', 'Leeftijd')
    set(handles.underage, 'String', 'Jonger dan 18 jaar')
    set(handles.overage, 'String', 'Ouder dan 18 jaar')
    set(handles.text5, 'String', 'e-mailadres')
    set(handles.text6, 'String', 'skypenaam')
    set(handles.close, 'String', 'Sluiten')
    set(handles.uibuttongroup3, 'Title', 'Talen')
end

% --- Executes on button press in Eng.
function Eng_Callback(hObject, eventdata, handles)
% hObject    handle to Eng (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of Eng
if get(hObject, 'Value')
    set(handles.text2, 'String', 'Settings')
    set(handles.text3, 'String', 'Indicate which graphs you want to be displayed')
    set(handles.panel1, 'Title', 'Graphs')
    set(handles.stepcounter, 'String', 'Step counter')
    set(handles.text7, 'String', 'Day goal:')
    set(handles.uipanel4, 'Title', 'Step counter')
    set(handles.text8, 'String', 'Day goal')
    set(handles.text4, 'String', 'Possibility to change personal data:')
    set(handles.uipanel2, 'Title', 'Personal data')
    set(handles.uibuttongroup1, 'Title', 'Gender')
    set(handles.male, 'String', 'Male')
    set(handles.female, 'String', 'Female')
    set(handles.uibuttongroup2, 'Title', 'Age')
    set(handles.underage, 'String', 'Under 18')
    set(handles.overage, 'String', 'Over 18')
    set(handles.text5, 'String', 'email address')
    set(handles.text6, 'String', 'Skype name')
    set(handles.close, 'String', 'Close')
    set(handles.uibuttongroup3, 'Title', 'Languages')
end
