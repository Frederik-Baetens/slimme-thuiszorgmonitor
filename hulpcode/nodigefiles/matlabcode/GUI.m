function varargout = GUI(varargin)
% GUI MATLAB code for GUI.fig
%      GUI, by itself, creates a new GUI or raises the existing
%      singleton*.
%
%      H = GUI returns the handle to a new GUI or the handle to
%      the existing singleton*.
%
%      GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUI.M with the given input arguments.
%
%      GUI('Property','Value',...) creates a new GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before GUI_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to GUI_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GUI

% Last Modified by GUIDE v2.5 24-Nov-2016 15:14:02

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GUI_OpeningFcn, ...
                   'gui_OutputFcn',  @GUI_OutputFcn, ...
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


% --- Executes just before GUI is made visible.
function GUI_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to GUI (see VARARGIN)

% Choose default command line output for GUI
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% transmission information GUI_welcome
gw = findobj('Tag','GUI_welcome');
if ~isempty(gw)
    gwdata = guidata(gw);
    if get(gwdata.English, 'Value')
        set(handles.language_eng, 'Value', 1.0)
        language_eng_Callback(handles.language_eng, eventdata, handles)
    end
    set(handles.user_text, 'String', get(gwdata.NameEdit, 'String'))
    set(handles.goalnumber, 'String', get(gwdata.StepGoal, 'String'))
end

%logo = imread('LifeLine_blue3_1E3B71', 'png', 'BackgroundColor',[0.886 0.91 0.953]);
%imshow(logo, 'Parent',handles.logo);


% UIWAIT makes GUI wait for user response (see UIRESUME)
% uiwait(handles.GUI);


% --- Outputs from this function are returned to the command line.
function varargout = GUI_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

% lay-out implementation
all_toggle = findall(0,'Style','togglebutton');
all_push = findall(0,'Style','pushbutton');
all_text = findall(0,'Style','text');
all_panels = findall(0,'Type','uipanel');
all_button_groups = findall(0,'Type','uibuttongroup');

set(handles.GUI,...
'units', 'normalized',...
'OuterPosition', [0 0 1 1],...
'Color',[0.886 0.91 0.953]);

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
'ForegroundColor',[1 1 1]);

set(all_panels,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',18,...
'ForegroundColor',[1 1 1]);

set(all_button_groups,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',18,...
'ForegroundColor',[1 1 1]);

set(handles.text4, 'Backgroundcolor',[0.886 0.91 0.953],...
    'FontSize', 16, 'ForegroundColor', [0 0 0])

set(handles.text5, 'Backgroundcolor',[0.886 0.91 0.953],...
    'FontSize', 16, 'ForegroundColor', [0 0 0])

set(handles.text6, 'Backgroundcolor',[0.886 0.91 0.953],...
    'FontSize', 12, 'ForegroundColor', [0 0 0])

set(handles.text7, 'Backgroundcolor',[0.886 0.91 0.953],...
    'FontSize', 12, 'ForegroundColor', [0 0 0])

set(handles.text8, 'Backgroundcolor',[0.886 0.91 0.953],...
    'FontSize', 12, 'ForegroundColor', [0 0 0])

set(handles.text10, 'Backgroundcolor',[0.886 0.91 0.953],...
    'FontSize', 12, 'ForegroundColor', [0 0 0])

set(handles.text9, 'Backgroundcolor',[0.447 0.545 0.729],...
    'FontSize', 12, 'ForegroundColor', [1 1 1])

set(handles.text11, 'Backgroundcolor',[0.886 0.91 0.953],...
    'FontSize', 12, 'ForegroundColor', [0 0 0])


% Mailen/skypen in geval van nood
alarmsituatie = true;
global skype_adres mail_adres
skype_adres = '';
mail_adres = '';

%Werkende skype_implementatie

h = findobj('Tag','GUI_welcome');
if ~isempty(h)
    GUI_welcome_data = guidata(h);
    skype_adres = get(GUI_welcome_data.Skype,'String');
    mail_adres = get(GUI_welcome_data.email,'String');
end

    
if alarmsituatie
    if ~isempty(skype_adres)
        skypen(skype_adres)
    else
        mailen(mail_adres)
    end
end
            
            
% axes_stappenteller implementation

% initialisatie  
max_stappen = 564;
gw = findobj('Tag','GUI_welcome');
    
interval = 10^(floor(log10(max_stappen)));
if mod(max_stappen,interval) == 0
    Ticks_x = [0:interval:(max_stappen+interval)];
else
    Ticks_x = [0:interval:max_stappen, max_stappen];
end

axis(handles.axes_stappenteller,[0, max_stappen, 0, 2])
set(handles.axes_stappenteller,'XTick',Ticks_x)

if ~isempty(gw)
    gwdata = guidata(gw);
    max_stappen = 500 ;% get(gwdata.edit2, 'String'); % via input
end

%pipeline_stappenteller = fopen('stappipe','r');
%pipeline_ppg = fopen('ekgpipe','r');
%pipeline_ecg = fopen('popipe','r');





function graphstappenteller(handles, max_stappen, current)

to_color = current/max_stappen;
X = [0;
     to_color;
     to_color;
     1];
Y = [2;
     2;
     0;
     0];
area(X,Y,'Parent',handles.axes_stappenteller);


% --- Executes on button press in help_ecg.
function help_ecg_Callback(hObject, eventdata, handles)

% info ecg

% hObject    handle to help_ecg (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
info_ecg;


% --- Executes on button press in help_stappenteller.
function help_stappenteller_Callback(hObject, eventdata, handles)

% info axes_stappenteller

% hObject    handle to help_stappenteller (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
info = get(hObject, 'Value');

lijst_stappen = [7 167 243 298 465 815];
setappdata(handles.help_stappenteller,'lijst_stappen',lijst_stappen);

if info
    info_stappenteller
end


% --- Executes on button press in reset_button.
function reset_button_Callback(hObject, eventdata, handles)

% resetknop

% hObject    handle to reset_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject, 'Value')
    cla
end
    


% --- Executes on button press in safe_button.
function safe_button_Callback(hObject, eventdata, handles)

% opslaan

% hObject    handle to safe_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in settings_button.
function settings_button_Callback(hObject, eventdata, handles)

% instellingen

% hObject    handle to settings_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global skype_adres mail_adres
if get(hObject, 'Value')
    Instellingen
    h = findobj('Tag','Instellingen');
    if ~isempty(h)
        inst_data = guidata(h);
        skype_adres = get(inst_data.Skype,'String');
        mail_adres = get(inst_data.email,'String');
    end
end

% --- Executes on button press in logoff_button.
function logoff_button_Callback(hObject, eventdata, handles)

%afmelden

% hObject    handle to logoff_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject, 'Value')
    afsluiten = questdlg('Deze gebruiker afsluiten?');
    switch afsluiten
        case 'Yes'
            GUI_welcome
            close(GUI)
            GUI_welcome
    end
end


% --- Executes on button press in language_nl.
function language_nl_Callback(hObject, eventdata, handles)

% taalkeuze Nederlands
% hObject    handle to language_nl (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of language_nl
Nederlands = get(hObject, 'Value');
if Nederlands
    set(handles.language_group, 'Title', 'Talen')
    set(handles.choice_panel, 'Title', 'Keuzemenu')
    set(handles.safe_button, 'String', 'Opslaan')
    set(handles.settings_button, 'String', 'Instellingen')
    set(handles.logoff_button, 'String', 'Afmelden')
    set(handles.Skype, 'String', 'Noodgeval: skype')
    set(handles.text9, 'String', '[stappen]')
    set(handles.text4, 'String', 'Elektrocardiogram (ECG)')
    set(handles.text6, 'String', '[samplenumber]')
    set(handles.text7, 'String', '[samplenumber]')
    set(handles.goal, 'String', 'Gekozen dagdoel:')
    set(handles.text14, 'String', 'stappen')
end

% --- Executes on button press in language_eng.
function language_eng_Callback(hObject, eventdata, handles)

% taalkeuze engels

% hObject    handle to language_eng (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of language_eng
Engels = get(hObject, 'Value');
if Engels
    set(handles.language_group, 'Title', 'Languages')
    set(handles.choice_panel, 'Title', 'Menu')
    set(handles.safe_button, 'String', 'Save')
    set(handles.settings_button, 'String', 'Settings')
    set(handles.logoff_button, 'String', 'Sign out')
    set(handles.user_panel, 'Title', 'User')
    set(handles.functions_panel, 'Title', 'Other functions')
    set(handles.Skype, 'String', 'Emergency: skype')
    set(handles.text9, 'string', '[steps]')
    set(handles.text4, 'String', 'Electrocardiogram (ECG)')
    set(handles.text6, 'String', '[samplenumber]')
    set(handles.text7, 'String', '[samplenumber]')
    set(handles.goal, 'String', 'Chosen goal:')
    set(handles.text14, 'String', 'steps')
end

function signal = datainlezing(purpose)
if strcmp(purpose,'ecg')
    signal = csvread('100.csv');
elseif strcmp(purpose,'ppg')
    signal = csvread('BVP.csv');
elseif strcmp(purpose,'stp');
    signal = csvread('stappenteller_data.csv');
end

function creategraph(signal_piece,np,nb_interval,spec_axes, lh, lb, margin, handles)
% signal_piece      vector met datapunten (y-waarden)
% np                aantal punten per datapakket
% nb_interval       nummer van het interval
% spec_axes         specifieer de assen waar de grafiek moet komen

button_state_start = get(handles.start_button,'Value');

i = 0;
y = -inf*ones(1,np);

while i ~= length(signal_piece) && button_state_start == 1
    
    i = i + 1;
    
    x_line = [(nb_interval-1)*(np-margin) + rem(i-1,np)+12, (nb_interval-1)*(np-margin) + rem(i-1,np)+12];

    y_line = [-500 500];

    l = line(x_line,y_line,'Color','r','LineWidth',2,...
        'Parent', spec_axes);

    g = line([(nb_interval-1)*(np-margin) + rem(i-1,np)+2, (nb_interval-1)*(np-margin) + rem(i-1,np)+2],y_line,'Color','w',...
        'LineWidth',14, 'Parent', spec_axes);
    
    ix = rem(i-1,np)+1;
    y(ix) = signal_piece(i); % <- nieuwe data
    set(lh,'ydata',y,'Parent',spec_axes);
    set(lb,'xdata',[ix,ix],'Parent',spec_axes);
    pause(0.0001);
    
    delete(l)

    delete(g)
end

% --- Executes on button press in start_button.
function start_button_Callback(hObject, eventdata, handles)

% Start- en stopknop

% hObject    handle to start_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of start_button
button_state_start = get(hObject,'Value');
%signal_ppg = datainlezing('ppg');
%signal_ppg = signal_ppg(6.195E5:6.277E5);
%signal_ecg = datainlezing('ecg');
%signal_stap = datainlezing('stp');

pipeline_ecg = fopen('popipe','r')

if button_state_start
    set(hObject,'String','Stop');
    
    % INITIALISATIE VARIABELEN
    
    % ALGEMEEN
    
    turn = 0;
    np = 11;
    margin = 1;
    nb_sec = 4;
    start_point = 0;
    stop_point = (4*np)*nb_sec;
    ymin = -500;
    ymax = 5000;
    max_interval = (stop_point - start_point)/np;
    axis(handles.axes_ppg, [start_point, stop_point, ymin, ymax]);
    %axes(handles.axes_ecg, [start_point, stop_point, -1.5, 1.5]);
    
    % PPG
    
    inputlist_red = [];
    peaks = [];
    hr = [];
    CorrHR =[];
    listnb = 0;
    
    % ECG
    
    %STAPPENTELLER
    
    steplist = [];
    nb_steps = 3;
    inputlist_stap = [];
    threshold = 1.5; % via input
    prev_sample = 1;
    max_stappen = 500;
    
    % EINDE INITIALISATIE VARIABELEN
    
    while get(hObject,'Value')
        
        % VERSIE MET PIPELINE
        signal_piece_ecg = fscanf(pipeline_ecg,'%f',[1,32]);
        %signal_ppg = fscanf(pipeline_ppg,'%f',[1,32]);
        %signal_stap = fscanf(pipeline_stappenteller,'%f',[1,32]);
        
        nb_interval = rem(turn,stop_point) + 1;
        
        if mod(nb_interval,max_interval)==0
            start_point = stop_point;
            stop_point = stop_point+(4*np*nb_sec);
            xlim(handles.axes_ppg, [start_point, stop_point]);
            xlim(handles.axes_ecg, [start_point, stop_point]);
        end

        
        if turn == 0
            begin = 1;
            interval_points = np;
        else
            begin = turn*np + 1 - margin;
            interval_points = np+margin;
        end
        
        ending = turn*np + np;
        
        x = [begin:ending];
        y = -inf*ones(size(x));
        lh = line(x,y,...
            'markersize',5,...
            'linestyle','-');
        lb = line([inf,inf],[-2,5]);
        shg;
        
        %signal_piece_ppg = signal_ppg(begin:ending);
        %signal_piece_ecg = signal_ecg(begin:ending);
        %signal_piece_stap = signal_stap(begin:ending);
        
%        inputlist_red = [inputlist_red; signal_piece_ppg];
        
%         % BEGIN PPG
%         
%         A = [inputlist_red(end)<0,inputlist_red(end-10) >0]
%         
%         if inputlist_red(end) < 0 && inputlist_red(end-10) > 0 && length(inputlist_red) > listnb
%             
%             listnb = length(inputlist_red);
%             if length(hr) <= 5
%                 if isempty(peaks)
%                     [ToBeAdded,SampNbNewPeak,SampNbExtraPeak,NewHR,NewCorrHR] = POM_GetIntervalAnalysis2(inputlist_red, 0, hr);
%                 else
%                     [ToBeAdded,SampNbNewPeak,SampNbExtraPeak,NewHR,NewCorrHR] = POM_GetIntervalAnalysis2(inputlist_red, peaks(end), hr);
%                 end
%                 
%             end
%             
%             if length(hr) > 5
%                 [ToBeAdded,SampNbNewPeak,SampNbExtraPeak,NewHR,NewCorrHR] = POM_GetIntervalAnalysis2(inputlist_red, peaks(end), hr((end-4):end));
%             end
%             
%             if ToBeAdded == true
%                 if ~(SampNbExtraPeak == 0)
%                     peaks(end+1) = SampNbExtraPeak;
%                     hr(end+1) = NewHR;
%                     CorrHR(end+1) = NewCorrHR;
%                 end
%                 
%                 peaks(end+1) = SampNbNewPeak;
%                 hr(end+1) = NewHR;
%                 CorrHR(end+1) = NewCorrHR;
%                 
%             end
%             
%             hr
%         end
%     
%         % EINDE PPG
        
        % BEGIN ECG
        
        
        % EINDE ECG
        
%         % BEGIN STAPPENTELLER
%         inputlist_stap = [inputlist_stap;signal_piece_stap];
% 
%         [stap_searchinterval, start_sample] = STAP_GetSearchInterval(inputlist_stap, threshold);
%         [to_be_added, samplenumber] = stappenteller(stap_searchinterval, start_sample, prev_sample);
% 
%         if to_be_added
%             
%             steplist = [steplist samplenumber];
%             nb_steps = nb_steps + 1;
%             graphstappenteller(handles, max_stappen, nb_steps);
%             drawnow;
%         end
%         
%         prev_sample = samplenumber;
%         
%         % EINDE STAPPENTELLER
%         
        creategraph(signal_piece_ecg,interval_points,nb_interval,handles.axes_ppg, lh, lb, margin, handles);
        
        turn = turn + 1;
    end
else
    set(hObject,'String','Start');
    cla;
end


% --- Executes on button press in help_ppg.
function help_ppg_Callback(hObject, eventdata, handles)

% info ppg

% hObject    handle to help_ppg (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject, 'Value')
    info_PPG
end

% --- Executes on button press in help_heartrate.
function help_heartrate_Callback(hObject, eventdata, handles)

% info hartritme

% hObject    handle to help_heartrate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if get(hObject, 'Value')
    info_heartrate
end


% --- Executes on button press in Skype.
function Skype_Callback(hObject, eventdata, handles)
% hObject    handle to Skype (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global skype_adres
if get(hObject, 'Value')
    skypen(skype_adres)
end
