FROM osixia/openldap:1.5.0

ENV LDAP_ORGANISATION="Northwind Manufacturing"
ENV LDAP_DOMAIN="northwind.local"
ENV LDAP_ADMIN_PASSWORD="Password123!"

COPY bootstrap.ldif /container/service/slapd/assets/config/bootstrap/ldif/custom/bootstrap.ldif

EXPOSE 389
