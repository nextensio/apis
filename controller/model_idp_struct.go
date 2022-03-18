/*
 * Controller APIs
 *
 * APIs to act on Nextensio Controller
 *
 * API version: 1.0.0
 * Contact: development@nextensio.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type IdpStruct struct {
	Provider string `json:"Provider"`
	Name string `json:"Name"`
	Idp string `json:"Idp"`
	Policy string `json:"Policy"`
	Domain string `json:"Domain"`
	Group string `json:"Group"`
	Auth string `json:"Auth"`
	Jwks string `json:"Jwks"`
	Token string `json:"Token"`
	Issuer string `json:"Issuer"`
	Sso string `json:"Sso"`
	Audience string `json:"Audience"`
	Client string `json:"Client"`
	Secret string `json:"Secret"`
	Cert string `json:"Cert"`
	Keyid string `json:"Keyid"`
}
