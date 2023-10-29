// MTN MoMo Cameroon API Client

class MTNMoMoAPIClient {
  constructor(userId, userSecret, primaryKey) {
    this.userId = userId;
    this.userSecret = userSecret;
    this.primaryKey = primaryKey;
  }

  // Authenticate with the MTN MoMo Cameroon API
  async authenticate() {
    const response = await fetch('https://momoapi.mtn.com/v1_0/auth/token', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.userSecret}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        userId: this.userId,
        primaryKey: this.primaryKey
      })
    });

    const data = await response.json();

    if (response.status === 200) {
      this.authToken = data.token;
      return true;
    } else {
      return false;
    }
  }

  // Perform a MoMo funds transfer
  async transferFunds(sender, recipient, amount) {
    if (!this.authToken) {
      await this.authenticate();
    }

    const response = await fetch('https://momoapi.mtn.com/v1_0/disbursements', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.authToken}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        sender: sender,
        recipient: recipient,
        amount: amount
      })
    });

    const data = await response.json();

    if (response.status === 200) {
      return {
        transactionId: data.transactionId,
        status: data.status
      };
    } else {
      return {
        error: data.error
      };
    }
  }
}
