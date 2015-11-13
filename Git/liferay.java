public class ShibbolethAutoLogin implements AutoLogin {
  
          public String[] login(HttpServletRequest req, HttpServletResponse res)
                  throws AutoLoginException {
  
                  String[] credentials = null;
                  // you can pull the userId from the REMOTE_USER or other parameter
  //              String userId = req.getHeader(USCPropsUtil.USC_AUTH_SHIB_UID);
                 String userId = req.getHeader("shib-person-uid");
                 String uscpvid = req.getHeader("shib-uscperson-uscownerpvid");
                 String mail = req.getHeader("shib-person-mail");
                 String displayName = req.getHeader("shib-person-displayname");
                 String passwd = null;
                 String userName = req.getParameter("userName");
 
 userId = uscpvid;
                 if (userId == null || userId.length() < 1) {
                         _log.error("Did not receive uid from Shibboleth");
                         return credentials;
                 }
 
                 try {
                         if (Validator.isNotNull(userId)) {
                                 credentials = new String[3];
 // This allows the omniadmin to impersonate another user. I have a separate loginform
 // for admins that has a field for the impersonate userId.  FYI: a non-omniadmin would
 // not be able to use that login form
                                 if (OmniadminUtil.isOmniadmin(userId)) {
                                          _log.error(userId+" is an Omniadmin!");
                                         if (userName != null &&  userName.length() > 0) {
                                                 _log.error("impersonating: "+userName);
                                                 credentials[0] = userName;
                                         }
                                         else {
                                                 credentials[0] = userId;
                                         }
                                 }
                                 User user = UserLocalServiceUtil.getUserById(credentials[0]);
                                 credentials[1] = user.getPassword();
                                 credentials[2] = Boolean.TRUE.toString();
 
                         }
 
                         return credentials;
                 }
                 catch (NoSuchUserException e) {
                 }
                 catch (Exception e) {
                         _log.error(StackTraceUtil.getStackTrace(e));
                         throw new AutoLoginException(e);
                }
                 try {
                         String creatorUserId = null;
                         String companyId = PortalUtil.getCompany(req).getCompanyId();
                         boolean autoUserId = false;
                        boolean autoPassword = false;
                         // we have to set the password to something, replace this in the
                         // future with something smarter
                         String password1 = "gotrojans";
                         String password2 = "gotrojans";
                         boolean passwordReset = false;
                         String emailAddress = mail;
                         Locale locale = Locale.US;
                         String firstName = displayName;
                         String middleName = null;
                         String lastName = ".";
                         String nickName = null;
                         String prefixId = null;
                         String suffixId = null;
                         boolean male = true;
                         int birthdayMonth = Calendar.JANUARY;
                         int birthdayDay = 1;
                         int birthdayYear = 1970;
                        String jobTitle = null;
                         String organizationId = null;
                         String locationId = null;
                         boolean sendEmail = false;
 
 
                         _log.error("calling: LDAPImportUtil.addOrUpdateUser()");
 
                         // setting password to null returns errors (actually null)
                         User user = UserLocalServiceUtil.addUser(
                                 creatorUserId, companyId, autoUserId, userId, autoPassword,
                                 password1, password2, passwordReset, emailAddress, locale,
                                 firstName, middleName, lastName, nickName, prefixId,
                                suffixId, male, birthdayMonth, birthdayDay, birthdayYear,
                                 jobTitle, organizationId, locationId, sendEmail);
 
 
                         if (user == null) {
                                 _log.error("LDAPImportUtil.addOrUpdateUser() returned null");
                         }
                         else {
                                 // we want a null password but this is not working - why?
                                 user.setPassword(null);
                         }
 
                        credentials = new String[3];
                        credentials[0] = userId;
                        credentials[1] = password1;
                        credentials[2] = Boolean.FALSE.toString();

                        return credentials;
                }
               catch (Exception e) {
                        _log.error(StackTraceUtil.getStackTrace(e));
                        _log.error(StackTraceUtil.getStackTrace(e));
                        throw new AutoLoginException(e);
                }
        }
}



