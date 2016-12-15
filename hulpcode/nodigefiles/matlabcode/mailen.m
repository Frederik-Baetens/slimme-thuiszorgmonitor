function mailen( mailadres )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here

myaddress = 'peno3.software@gmail.com';
mypassword = 'peno3software';
setpref('Internet','E_mail',myaddress);
setpref('Internet','SMTP_Server','smtp.gmail.com');
setpref('Internet','SMTP_Username',myaddress);
setpref('Internet','SMTP_Password',mypassword);
props = java.lang.System.getProperties;
props.setProperty('mail.smtp.auth','true');
props.setProperty('mail.smtp.socketFactory.class', ...
    'javax.net.ssl.SSLSocketFactory');
props.setProperty('mail.smtp.socketFactory.port','465');

gw = findobj('Tag','GUI_welcome');
gwdata = guidata(gw);

if ~isempty(gwdata)
    naam_patient = get(gwdata.NameEdit,'String');
    
    if get(gwdata.Nederlands,'Value')
               
        if get(gwdata.Male,'Value')
            geslacht = 'hem';
        else
            geslacht = 'haar';
        end
        
        text_mail = strcat(naam_patient,...
        ' heeft op de noodknop geduwd van de thuiszorgmonitor LifeLine. Gelieve met ',...
        geslacht,' zo snel mogelijk contact op te nemen.');
    
        sendmail(mailadres,'Hallo',...
        text_mail,...
        'Met vriendelijke groeten',...
        'LifeLine');
    
    else
        
        if get(gwdata.Male,'Value')
            geslacht = 'him';
        else
            geslacht = 'her';
        end
        
        text_mail = strcat(naam_patient,...
            'pushed the emergency button of monitoring programm LifeLine. Please contact ',...
            geslacht,' as soon as possible.');
        
        sendmail(mailadres,'Hello',...
            text_mail,...
            'Yours sincerely',...
            'LifeLine');
        
    end

end

