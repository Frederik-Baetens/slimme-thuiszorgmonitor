function varargout = GUI_welcome(varargin)
% GUI_WELCOME MATLAB code for GUI_welcome.fig
%      GUI_WELCOME, by itself, creates a new GUI_WELCOME or raises the existing
%      singleton*.
%
%      H = GUI_WELCOME returns the handle to a new GUI_WELCOME or the handle to
%      the existing singleton*.
%
%      GUI_WELCOME('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUI_WELCOME.M with the given input arguments.
%
%      GUI_WELCOME('Property','Value',...) creates a new GUI_WELCOME or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before GUI_welcome_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to GUI_welcome_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GUI_welcome

% Last Modified by GUIDE v2.5 24-Nov-2016 14:45:21

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GUI_welcome_OpeningFcn, ...
                   'gui_OutputFcn',  @GUI_welcome_OutputFcn, ...
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


% --- Executes just before GUI_welcome is made visible.
function GUI_welcome_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to GUI_welcome (see VARARGIN)

% Choose default command line output for GUI_welcome
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% logo = imread('Logo.jpg'); %,'BackgroundColor',[0.886 0.91 0.953]);
% imshow(logo, 'Parent', handles.Logo);
logo = imread('LifeLine_blue3_1E3B71', 'png', 'BackgroundColor',[0.886 0.91 0.953]);
imshow(logo, 'Parent',handles.Logo);


% UIWAIT makes GUI_welcome wait for user response (see UIRESUME)
% uiwait(handles.GUI_welcome);


% --- Outputs from this function are returned to the command line.
function varargout = GUI_welcome_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

% lay-out

all_toggle = findall(0,'Style','togglebutton');
all_push = findall(0,'Style','pushbutton');
all_text = findall(0,'Style','text');
all_panels = findall(0,'Type','uipanel');
all_button_groups = findall(0,'Type','uibuttongroup');
all_radiobuttons = findall(0, 'Style','radiobutton');
all_edit = findall(0, 'Style','edit');

set(handles.GUI_welcome,...
'units', 'normalized',...
'OuterPosition', [0 0 1 1],...
'Color',[0.886 0.91 0.953]);

set(all_edit, 'FontSize', 16)

set(all_radiobuttons,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize', 16);

set(all_toggle,...
'BackgroundColor',[0.118 0.231 0.443],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

set(all_push,...
'BackgroundColor',[0.118 0.231 0.443],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

set(all_text,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',16,...
'ForegroundColor',[0 0 0]);

set(all_panels,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',18,...
'ForegroundColor',[1 1 1]);

set(all_button_groups,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',18,...
'ForegroundColor',[1 1 1]);

set(handles.text8,'BackgroundColor',[0.886 0.91 0.953],...
 'ForegroundColor', [0 0 0],...
 'FontSize',14);

set(handles.text2,'BackgroundColor',[0.886 0.91 0.953],...
 'ForegroundColor', [0 0 0],...
 'FontSize',32);




% --- Executes on button press in Nederlands.
function Nederlands_Callback(hObject, eventdata, handles)
% hObject    handle to Nederlands (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of Nederlands
Nederlands = get(hObject, 'Value');
if Nederlands;
    set(handles.text2 , 'String', 'Welkom');
    set(handles.uibuttongroup1, 'Title', 'Talen');
    set(handles.uipanel1, 'Title', 'Persoonlijke gegevens');
    set(handles.uibuttongroup2, 'Title', 'Geslacht')
    set(handles.text3, 'String', 'Naam*');
    set(handles.Male, 'String', 'Man');
    set(handles.Female, 'String', 'Vrouw');
    set(handles.Save, 'String', 'Opslaan');
    set(handles.ShutDown, 'String', 'Afsluiten');
    set(handles.NoAdult, 'String', 'Jonger dan 18');
    set(handles.Adult, 'String', 'Ouder dan 18');
    set(handles.uipanel2, 'Title', 'Stappenteller');
    set(handles.text4, 'String', 'Dagdoel');
    set(handles.uibuttongroup3, 'Title', 'Leeftijd');
    set(handles.uipanel3, 'Title', 'Noodsituatie');
    set(handles.text6, 'String', 'Gelieve deze gegevens door te geven om in noodsituaties een verwittiging te kunnen sturen. Het e-mailadres en de skypenaam zijn van de persoon die gecontacteerd moet worden in geval van nood.');
    set(handles.text5, 'String', 'e-mailadres*');
    set(handles.uibuttongroup4, 'Title', 'Verwittigingswijze');
    set(handles.MailEmergency, 'String', 'e-mail');
    set(handles.SkypeEmergency, 'String', 'Skype');
    set(handles.text8, 'String', '*Verplicht veld');
    set(handles.text9, 'String', 'Skypenaam');
    set(handles.steps,'String','stappen');
end


% --- Executes on button press in English.
function English_Callback(hObject, eventdata, handles)
% hObject    handle to English (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of English
Engels = get(hObject, 'Value');
if Engels
    set(handles.text2 , 'String', 'Welcome');
    set(handles.uibuttongroup1, 'Title', 'Languages');
    set(handles.uipanel1, 'Title', 'Personal data');
    set(handles.uibuttongroup2, 'Title', 'Gender');
    set(handles.text3, 'String', 'Name*');
    set(handles.Male, 'String', 'Male');
    set(handles.Female, 'String','Female');
    set(handles.Save, 'String', 'Save');
    set(handles.ShutDown, 'String', 'Shut down');
    set(handles.NoAdult, 'String', 'Under 18');
    set(handles.Adult, 'String', 'Over 18');
    set(handles.uipanel2, 'Title', 'Step counter');
    set(handles.text4, 'String', 'Day goal');
    set(handles.uibuttongroup3, 'Title', 'Age');
    set(handles.uipanel3, 'Title', 'In case of emergency');
    set(handles.text6, 'String', 'Please fill in to send a message in case of emergency. The Skype name and email address are from the person who has to be contacted.');
    set(handles.text5, 'String', 'email address*');
    set(handles.uibuttongroup4, 'Title', 'Way of communication');
    set(handles.MailEmergency, 'String', 'email');
    set(handles.SkypeEmergency, 'String', 'Skype');
    set(handles.text8, 'String', '*Mandatory field');
    set(handles.text9, 'String', 'Skype name');
    set(handles.steps, 'String', 'steps');
end



function NameEdit_Callback(hObject, eventdata, handles)
% hObject    handle to NameEdit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of NameEdit as text
%        str2double(get(hObject,'String')) returns contents of NameEdit as a double


% --- Executes during object creation, after setting all properties.
function NameEdit_CreateFcn(hObject, eventdata, handles)
% hObject    handle to NameEdit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Save.
function Save_Callback(hObject, eventdata, handles)
% hObject    handle to Save (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if isempty(get(handles.NameEdit, 'String')) || isempty(get(handles.email, 'String'))
    if get(handles.Nederlands, 'Value') == 1.0 
        msgbox('Gelieve alle verplichte velden in te vullen!', 'Opgelet', 'error')
    elseif get(handles.English, 'Value') == 1.0
        msgbox('Please fill all mandatory fields!', 'Error', 'error')
    end
else    
    GUI
    close(GUI_welcome)
    GUI
end


% --- Executes on button press in ShutDown.
function ShutDown_Callback(hObject, eventdata, handles)
% hObject    handle to ShutDown (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject, 'Value')
    if get(handles.Nederlands, 'Value')
        closing = questdlg('Afsluiten?');
    else
        closing = questdlg('Shut down?');
    end
    switch closing
        case 'Yes'
            close(GUI_welcome)
    end
end


% --- Executes during object creation, after setting all properties.
function GUI_welcome_CreateFcn(hObject, eventdata, handles)
% hObject    handle to GUI_welcome (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called



function StepGoal_Callback(hObject, eventdata, handles)
% hObject    handle to StepGoal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of StepGoal as text
%        str2double(get(hObject,'String')) returns contents of StepGoal as a double


% --- Executes during object creation, after setting all properties.
function StepGoal_CreateFcn(hObject, eventdata, handles)
% hObject    handle to StepGoal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
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
