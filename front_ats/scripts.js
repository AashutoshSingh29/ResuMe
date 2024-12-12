function viewTemplate(templateId) {
  document.getElementById('editor').style.display = 'block';
  document.getElementById('template-selection').style.display = 'none';

  let documentUrl = "";

  if (templateId === 1) {
      // Replace with your SharePoint/OneDrive link (with edit permissions)
      documentUrl = "https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2F1drv.ms%2Fw%2Fc%2Fe5b3375641c314bc%2FEeFXpigVWNpAlfhIDRHoA0UBxPIY7n6Sw7YyHSMOLsHIXQ&data=05%7C02%7Caashutosh.singhgautam%40in.bosch.com%7C9e5aed4ecf15412c9a0208dd1a9f5ff3%7C0ae51e1907c84e4bbb6d648ee58410f4%7C0%7C0%7C638695993983122937%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=0VEnLt3q%2B4fP%2B2mMSXpsbHyiGDKs3mRy2%2FQ%2Fex53tHA%3D&reserved=0";
  }

  // Set the src of the iframe to open the Word document in Word Online
  document.getElementById('word-editor').src = documentUrl;
}
