require 'spec_helper'
require 'net/http'

describe "HA Proxy Stats" do
  describe service('haproxy') do
    http = Net::HTTP.new('localhost', 1936)
    http.start do |http|
      request = Net::HTTP::Get.new('/')
      request.basic_auth 'user', 'pass'
      response, data = http.request(request)
      it { expect(response.code).to eq('200') }
    end
  end
end
