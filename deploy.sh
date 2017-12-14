#/bin/sh
ps aux|grep /home/ake/app/tomcat-mgr|grep -v grep|awk '{print $2}'|xargs kill -9

cp -r /home/ake/app/tomcat-mgr/webapps/mgr-weixin/WEB-INF/classes/conf mgr-weixin-conf
cp -r /home/ake/app/tomcat-mgr/webapps/mgr/WEB-INF/classes/conf mgr-conf

rm -rf /home/ake/app/tomcat-mgr/webapps/mgr-weixin/
cp -r park-mgr-saas/park-mgr-saas-weixin/target/park-mgr-saas-weixin /home/ake/app/tomcat-mgr/webapps/mgr-weixin
rm -rf /home/ake/app/tomcat-mgr/webapps/mgr-weixin/WEB-INF/classes/conf 
mv mgr-weixin-conf /home/ake/app/tomcat-mgr/webapps/mgr-weixin/WEB-INF/classes/conf

rm -rf /home/ake/app/tomcat-mgr/webapps/mgr/
cp -r park-mgr-saas/park-mgr-saas-web/target/park-mgr-saas-web /home/ake/app/tomcat-mgr/webapps/mgr
rm -rf /home/ake/app/tomcat-mgr/webapps/mgr/WEB-INF/classes/conf
mv mgr-conf /home/ake/app/tomcat-mgr/webapps/mgr/WEB-INF/classes/conf

/home/ake/app/tomcat-mgr/bin/startup.sh

tail -f /home/ake/app/tomcat-mgr/logs/catalina.out
