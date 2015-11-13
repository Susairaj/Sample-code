Security::
	class name..     class object...  class name..optional group id... 
Hide and show:
	<field name="patient_name" attrs="{'invisible':[('type','!=','patient')]}"/>
	<field name="student_name" attrs="{'invisible':[('type','!=','student')]}"/>------type=field
Call wizard by button:
	<button name="onchange_student_name" String="Test" type="object" />
Change the selection field to radio button:
	widget="radio"
	widget="image"
	widget="statusbar"
	
	
python version
  django-admin.py version
	
	
	
	PYTHON:
	
	http://runnable.com
	http://win32com.goermezer.de/
	http://www.programiz.com/python-programming
	https://www.python.org/
	http://www.codecademy.com
	http://interactivepython.org
	http://www.secnetix.de/olli/Python/
	http://programarcadegames.com/index.php?lang=en&chapter=example_code_sprite
	http://sandbox.mc.edu/~bennet/python/code/
	https://cloud.google.com/appengine/docs/python/tools/uploadinganapp
	http://www.java2s.com/Code/Python/CatalogPython.htm
	http://www.pythonforbeginners.com/code-snippets-source-code/python-code-examples
	http://www.pythontutor.com/visualize.html#mode=edit
	courses.cs.washington.edu/courses/cse142/11au/python.shtml
	http://www.bogotobogo.com/python/python_network_programming_server_client.php
	http://mortoray.com/
	http://mortoray.com/
	http://interactivepython.org/runestone/static/pythonds/index.html
	https://inventwithpython.com/hacking/chapters/
	http://www.catb.org/esr/faqs/hacker-howto.html#teach_hack
	http://thierry-godin.developpez.com/openerp/openerp-xmlrpc-php-en/
	http://pymotw.com/2/zipfile/
	http://www.bogotobogo.com/python/python_dictionary_comprehension_with_zip_from_list.php
	http://www.javaxp.com/search/label/mail
	http://sourceforge.net/projects/meeralferay/files/
	https://doc.odoo.com/6.0/developer/6_22_XML-RPC_web_services/
	http://snipplr.com/view/17605/openerp-xmlrpc-web-services/
	https://github.com/DeBortoliWines/openerp-java-api/blob/master/src/com/debortoliwines/openerp/api/OpenERPCommand.java
	http://sourceforge.net/p/openerpjavaapi/wiki/Examples/
	https://bpaste.net/show/pJ6SCtfunRqoFmdmUOEf
	http://www.mkyong.com/python/python-read-xml-file-dom-example/
	http://pragtech.co.in/technologies/odoo-openerp.html
	http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
	http://pymotw.com/2/datetime/
	http://python-future.org/standard_library_imports.html
	http://pymbook.readthedocs.org/en/latest/
	https://www.djangosites.org/with-source/
	http://elweb.co/33-projects-that-make-developing-django-apps-awesome/
	http://innovationliferay.blogspot.in/2012/01/velocity-variables.html
	
	
	
	imdp.com
	wifi - wireless fidelity
	http://wire.besplatform.com/
	wbm site:
	odoo:http://wbm.besplatform.com
	password;;;wbm@15
	liferay:http://wbmpoc.besplatform.com
	vpn-wbm username and password::
	username  : flyingbridge
    password  : Web3portalZ
	vpn-wbm site::
	http://10.10.10.2:8069/ ---odoo
	http://10.10.10.2:8080 ---liferay
	site db password:
	 admin@wbmoore.com
		wbm@15
		 
	\\192.168.1.124\share
	http://localhost:8089/?debug=
	http://localhost:8069/web/database/selector
	http://10.10.10.02:8069/web?#id=13&view_type=form&model=ir.module.module&action=37
	liferay-iframe:
	<iframe src="http://localhost:8069/loginweb?db=WBM&login=${permissionChecker.getUser().emailAddress}&redirect=web?#view_type=kanban&model=initiative.proposal&menu_id=329&action=425" width="100%" height="800"></iframe>
	<iframe src="http://www.bamboohr.com" width="100%" height="800"></iframe>
	odoo - iframe:
	<iframe marginheight="0" marginwidth="0" frameborder = "0" 
                src="http://wbm.besplatform.com/web?#view_type=kanban&model=initiative.proposal&menu_id=464&action=535" width="100%" height="1000"/>
				<iframe src="http://50.62.133.174:8069/loginweb?db=wbm&login=${permissionChecker.getUser().emailAddress}&redirect=web#page=0&limit=80&view_type=list&model=project.project&menu_id=428&action=493" width="100%" height="800"></iframe>

	
	http://wbmpoc.besplatform.com/web/wbmoore/department
	http://wbmpoc.besplatform.com/web/wbmoore/benefit-group
	
	google ip address:::
	http://173.194.37.50/
	
	Run odoo in commend line:
	python odoo.py -c debian/openerp-server.conf
	
	
	https://login.teamviewer.com/LogOn/#nav/computer/665061931/50565855
Email:tflyingbridge@wbmoore.com
Password :Web4portalZ



class replacement_code(models.Model):
    _name = 'replacement.code'
    name = fields.Many2one('replacement.reasoncode','Replacement Code')
    whos_fault = fields.Many2one('replacement.faults','Whos Fault')
    amount = fields.Float('Amount')
    total_amount = fields.Float('Total Amount',compute='find_total')
    sale_order_id = fields.Many2one('sale.order')
    
    @api.depends('amount')
    def find_total(self):
        for record in self:
            record.total_amount = (float(record.sale_order_id.amount_untaxed) * float(record.amount))/100
        return True

Liferay Image With content:
<table border="0" cellpadding="1" cellspacing="1" height="250" style="color: rgb(0, 0, 0); font-family: effra, sans-serif; font-size: 16px; line-height: normal;" width="550">
	<tbody>
		<tr>
			<td width="100"><img alt="" src="/documents/10181/0/SusanLaukat.jpg/7d83407f-d5d3-4b29-ba44-b28cb2dd8ffe?t=1425540440829" style="width: 100px; height: 133px;" /></td>
			<td>
			<p>Susan Laukat</p>

			<p>Human Resources Director Vernon Jeter recently announced that HR Generalist Susan Laukat has passed her Professional in Human Resources examination. Established by the Human Resource Certification Institute, this exam is considered so challenging that "half of all those who are qualified to sit for the test never pass it". This milestone represents hours of hard work and dedication for Susan, and truly demonstrates her skills, abilities and overall Human Resources knowledge. WB Moore wholeheartedly congratulates Susan on her accomplishment, and we look forward to greeting her as Susan Laukat, PHR!</p>
			</td>
		</tr>
	</tbody>
</table>
Liferay footer icon change:

<footer id="footer" role="contentinfo">
		<p class="powered-by">
		$themeDisplay.getPathThemeImages()
			#language ("powered-by") <a href="http://www.liferay.com" rel="external">wbmoore</a><span class="foot-logo"><img src="$themeDisplay.getPathThemeImages()/thumbnail.png" /></span>
		</p>
</footer>
Liferay:::::
boolean admin= actionRequest.isUserInRole("Administrator");
String userId = actionRequest.getRemoteUser();
User user1 = (User) actionRequest.getAttribute(WebKeys.USER);

To delete Pg user::
net user postgres /delete


Finding admin role from the users:]
for (User user : users) {
				List<Role> userRoles = user.getRoles();
	            for(Role r : userRoles){
	                if("Administrator".equalsIgnoreCase(r.getName())){

Find the current login user admin or not:::					
					PermissionChecker permissionChecker = PermissionThreadLocal.getPermissionChecker();
		permissionChecker.isOmniadmin();

		
		
Main prduct:
Manufacture
Make to order
Supplier
Components:
Buy 
Make to order
Supplier