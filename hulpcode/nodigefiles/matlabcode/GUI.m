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
end

%close(GUI_welcome)

% transmission information Instellingen
Inst = findobj('Tag', 'Instellingen');
if ~isempty(Inst)
    instdata = guidata(Inst);
    %hier moeten via het tablad instellingen de gewenste grafieken
    %geselecteerd worden.
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
'FontSize',14,...
'ForegroundColor',[1 1 1]);

set(all_push,...
'BackgroundColor',[0.118 0.231 0.443],...
'FontSize',14,...
'ForegroundColor',[1 1 1]);

set(all_text,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',14,...
'ForegroundColor',[1 1 1]);

set(all_panels,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

set(all_button_groups,...
'BackgroundColor',[0.447 0.545 0.729],...
'FontSize',16,...
'ForegroundColor',[1 1 1]);

% Mailen/skypen in geval van nood
% alarmsituatie = true;
% 
% h = findobj('Tag','GUI_welcome');
% if ~isempty(h)
%     GUI_welcome_data = guidata(h);
%     global skype_adres
%     skype_adres = get(GUI_welcome_data.Skype,'String');
%     mail_adres = get(GUI_welcome_data.email,'String');
% end
%     
% if alarmsituatie
%     if ~isempty(skype_adres)
%         skypen(skype_adres)
%     else
%         mailen(mail_adres)
%     end
% end


% % PPG
% 
% inputlist_red = [];
% inputlist_infrared= [];
% peaks = [];
% hr = [];
% CorrHR =[];
% listnb = 0;
% 
% filename = 'test_reading.txt';
% 
% while get(handles.start_button,'Value') == 1
%     
%     [inputlist_red, inputlist_infrared] = lezen_ppg(inputlist_red, inputlist_infrared, filename);
%     
%     if inputlist_red(end) < 0 && inputlist_red(end-10) > 0 && length(inputlist_red) > listnb
%         
%         listnb = length(inputlist_red);
%         [ToBeAdded,SampNbNewPeak,SampNbExtraPeak,NewHR,NewCorrHR] = POM_GetIntervalAnalysis(inputlist_red, peaks(end), hr(end-4:end));
%         
%         if ToBeAdded == true
%             if ~(SampNbExtraPeak == 0)
%                 peaks(end+1) = SampNbExtraPeak;
%                 hr(end+1) = NewHR;
%                 CorrHR(end+1) = NewCorrHR;
%             end
%             
%         peaks(end+1) = SampNbNewPeak;
%         hr(end+1) = NewHR;
%         CorrHR(end+1) = NewCorrHR;
%             
%         end
%     end
% end
            
            


% % axes_stappenteller implementation
% 
% % initialisatie  
% steplist = [];
% nb_steps = 1;
% inputlist = [1];
% threshold = 1.5; % via input
% prev_sample = 1;
% max_stappen = 564;
% gw = findobj('Tag','GUI_welcome');
%     
% interval = 10^(floor(log10(max_stappen)));
% if mod(max_stappen,interval) == 0
%     Ticks_x = [0:interval:(max_stappen+interval)];
% else
%     Ticks_x = [0:interval:max_stappen, max_stappen];
% end
% 
% axis(handles.axes_stappenteller,[0, max_stappen, 0, 2])
% set(handles.axes_stappenteller,'XTick',Ticks_x)
% 
% if ~isempty(gw)
%     gwdata = guidata(gw);
%     max_stappen = 500 ;% get(gwdata.edit2, 'String'); % via input
% end
% 
% C = 'initialisatie';
% while ~isempty(C)
%     % gegevenstroom komt binnen
%     fid = fopen('test_reading.txt', 'r') ;       % Open source file.
% 
%     C = str2double(fgetl(fid));                  % Read/discard line.
%     if isnan(C)
%         'lege file'
%         break
%     end
%     
%     inputlist(end+1) = C;
% 
%     buffer = fread(fid, Inf) ;                  % Read rest of the file.
%     fclose(fid);
% 
%     fid = fopen('test_reading.txt', 'w')  ;       % Open destination file.
%     fwrite(fid, buffer) ;                         % Save to file.
%     fclose(fid) ;
%     
%     
%     % input verwerking
%     [stap_searchinterval, start_sample] = STAP_GetSearchInterval(inputlist, threshold);
%     [to_be_added, samplenumber] = stappenteller(stap_searchinterval, start_sample, prev_sample);
%     
%     to_be_added = true;
%     
%     if to_be_added
%         
%         steplist = [steplist samplenumber];
%         nb_steps = nb_steps + 1;
%         nb_steps
%         graphstappenteller(handles, max_stappen, nb_steps);
%         drawnow;
%     end
%     prev_sample = samplenumber;
% end

% ECG - Initialisatie
tijd = 32;
sample_rate = 360;
lengte = tijd;
pauze = 0;
% graf = ECG; % Moet weg in finale versie, pipeline gebruiken
pipeline_ecg = fopen('ekgpipe','r');
'check'

xste_keer_doorlopen = 0;
vier_laatste_pieken = [];
tijdstip_laatste_piek = -10;

% PPG - initialisatie
inputlist_red = [];
inputlist_infrared= [];
peaks = [];
hr = [];
CorrHR =[];
listnb = 0;
%pipeline_ppg = fopen('popipe','r');

% while loop - Moet nog ppg en stappenteller bij
while 1~=2 % Moet andere voorwaarde worden: value van reset/start
    
    ECG_new = fscanf(pipeline_ecg,'%u',[1,32]);
    
    % result = [nr_hartslag gemiddelde_hartslag tijdstip_buitenbrengen nieuwe_pieken]
    result = testeenlijnecg(ECG_new,tijd,sample_rate,lengte,xste_keer_doorlopen,vier_laatste_pieken,tijdstip_laatste_piek);
    
    nr_hartslag = result(1);
    hartslag = result(2);

    set(handles.hartslag_text,'String',hartslag,'ForegroundColor','red');
  
    if hartslag == -1
        tijdstip_laatste_piek = result(3);

        vier_laatste_pieken = result(4:end);
        
        xste_keer_doorlopen = xste_keer_doorlopen + 1;
        continue
    end
    
    tijdstip_laatste_piek = result(3);

    vier_laatste_pieken = result(4:end);
    
    disp([nr_hartslag hartslag])
    
    xste_keer_doorlopen = xste_keer_doorlopen + 1;
    
    pause(pauze); % Voor testen, verwijderen in finale versie
    
    % PPG
    
%     % Nog lijst opsplitsen
%     [inputlist_red, inputlist_infrared] = fscanf('pipeline_ppg','r');
%     
%     if inputlist_red(end) < 0 && inputlist_red(end-10) > 0 && length(inputlist_red) > listnb
%         
%         listnb = length(inputlist_red);
%         [ToBeAdded,SampNbNewPeak,SampNbExtraPeak,NewHR,NewCorrHR] = POM_GetIntervalAnalysis(inputlist_red, peaks(end), hr(end-4:end));
%         
%         if ToBeAdded == true
%             if ~(SampNbExtraPeak == 0)
%                 peaks(end+1) = SampNbExtraPeak;
%                 hr(end+1) = NewHR;
%                 CorrHR(end+1) = NewCorrHR;
%             end
%             
%         peaks(end+1) = SampNbNewPeak;
%         hr(end+1) = NewHR;
%         CorrHR(end+1) = NewCorrHR;
%             
%         end
%     end
end



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
if get(hObject, 'Value')
    Instellingen
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
end

function signal = datainlezing()
signal = csvread('BVP.csv');

function creategraph(signal, start_point,stop_point,np,spec_axes, lh, lb, handles)
% signal            vector met datapunten (y-waarden)
% start_point       kolom v/d vector vanaf waar het signaal geanalyseerd
%                   wordt
% stop_point        kolom v/d vector tot waar het signaal geanalyseerd
%                   wordt
% np                data per frame
% spec_axes         specifieer de assen waar de grafiek moet komen
% Gegevens initialiseren
%axes(handles.axes_ecg);
global button_state_start
% temp_stop = start_point + np;

% % Plot voorbereiden
% ymin = -500;
% ymax = 500;
% axis(spec_axes, [start_point, temp_stop, ymin, ymax]);
% 
% x = 1:np;
% y = -inf*ones(size(x));
% lh = line(x,y,...
% 'markersize',5,...
% 'linestyle','-');
% lb = line([inf,inf],[-2,5]);
% shg;

i = 0;
while i ~= stop_point && button_state_start == 1

   i = i + 1;
   ix = rem(i-1,np)+1;
   y(ix) = signal(i) % <- nieuwe data
   [0:ix]
   set(lh,'ydata',y,'Parent',handles.axes_ecg);
   set(lb,'xdata',[0:ix],'Parent',handles.axes_ecg);
   pause(.0001);
end

% --- Executes on button press in start_button.
function start_button_Callback(hObject, eventdata, handles)

% Start- en stopknop

% hObject    handle to start_button (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of start_button
guidata(hObject,handles)
global button_state_start
button_state_start = get(hObject,'Value');
signal = datainlezing();
if button_state_start
    set(hObject,'String','Stop');
    
    % Plot voorbereiden
    
    while button_state_start
        
        ymin = -500;
        ymax = 500;
        start_point = 0;
        stop_point = 300;
        axis(handles.axes_ecg, [start_point, stop_point, ymin, ymax]);
        np = 640;

        x = 1:np;
        y = -inf*ones(size(x));
        lh = line(x,y,...
        'markersize',5,...
        'linestyle','-');
        lb = line([inf,inf],[-2,5]);
        shg;
        
        % xdata = [begin:ending];
        signal_piece = signal(1:360);

        creategraph(signal_piece,start_point,stop_point,np,handles.axes_ecg, lh, lb, handles);
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
